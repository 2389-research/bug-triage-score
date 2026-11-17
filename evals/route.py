# ABOUTME: Tests whether bug-triage-score's description wins routing against other skills.
# ABOUTME: Asks a tool-less claude -p which skill it would load first for each request.
"""Usage: uv run --no-project python evals/route.py --skill old=evals/arms/v1.md --skill new=SKILL.md [--reps 3]

Reads competitor descriptions from evals/routing/skills.txt (one "name: description" per line)
and requests from evals/routing/requests.json ({"text": ..., "expect": skill name}).
Prints one line per request and arm: hits/reps and the answers given.
"""
import argparse
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent


def description(skill_md):
    m = re.search(r"^description:\s*(.+)$", Path(skill_md).read_text(), re.M)
    return m.group(1).strip()


def ask(skills_text, request, model):
    prompt = (
        "You are choosing which skill to load before answering a request.\n"
        f"Available skills:\n{skills_text}\n\nRequest: {request}\n\n"
        "Reply with only the name of the one skill you would load first, or none."
    )
    out = subprocess.run(
        ["claude", "-p", "--safe-mode", "--tools", "", "--model", model, prompt],
        capture_output=True, text=True, stdin=subprocess.DEVNULL,
    ).stdout.strip()
    return out.splitlines()[0].strip("`* ") if out else "(empty)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", action="append", required=True)
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--model", default="sonnet")
    a = ap.parse_args()
    others = (HERE / "routing" / "skills.txt").read_text().strip()
    requests = json.loads((HERE / "routing" / "requests.json").read_text())
    jobs = []
    for spec in a.skill:
        arm, _, path = spec.partition("=")
        skills_text = others + f"\n- bug-triage-score: {description(path)}"
        for r in requests:
            for _ in range(a.reps):
                jobs.append((arm, r, skills_text))
    with ThreadPoolExecutor(8) as pool:
        answers = list(pool.map(lambda j: ask(j[2], j[1]["text"], a.model), jobs))
    tally = {}
    for (arm, r, _), ans in zip(jobs, answers):
        tally.setdefault((arm, r["text"], r["expect"]), []).append(ans)
    for (arm, text, expect), got in tally.items():
        hits = sum(g == expect for g in got)
        print(f"{arm:5} {hits}/{len(got)} expect={expect:18} got={got} :: {text[:60]}")


if __name__ == "__main__":
    main()
