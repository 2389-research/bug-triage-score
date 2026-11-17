# writing-skills checklist: bug-triage-score hardening round 2

Run with superpowers:writing-skills 7.0.2 (loaded via the Skill tool) on 2026-11-17.
The session has no todo tool, so this file tracks each checklist item. Results are in ../README.md.

## RED
- [x] Pressure scenarios with 3+ combined pressures, on a held-out fixture: `incident-standup` (time, sunk cost, authority, social), `audit-internal` (time, "don't over-engineer", absence)
- [x] Baselines at 5 reps: control and original skill on round-1 scenarios
- [x] New scenarios run without the skill and with v4; failures recorded verbatim in run `final.md` files
- [x] Patterns: ranges in rating cells, actions that contradict the score, per-code-path frequency

## GREEN
- [x] Name: letters, numbers, hyphens only
- [x] Frontmatter: name + description, description about 285 chars
- [x] Description starts "Use when", third person, triggers only
- [x] Description routing: 27/27 for old and current descriptions; unchanged
- [x] Keywords: code review, debugging, audits, QA, testing, edge case, file as issues
- [x] Overview with core principle: the score decides; fix size never enters it
- [x] Each change addresses a recorded failure (see README "What each version changed")
- [x] Form matches failure: recipe table for the decision, structural cells for the report, prohibitions only for discipline
- [x] Wording tested against a no-guidance control (control arm, 5 reps per scenario, every row read or script-checked)
- [x] Scenarios rerun with the skill; agents comply (v7: 10/10 on the ledgerly audits)

## REFACTOR
- [x] New rationalizations identified: "shows on every --help", "I'd rather not touch it"
- [x] Explicit counters added (frequency definition, `blocked: <reason>`)
- [x] Rationalization table built from all rounds
- [x] Red flags list
- [x] Meta-test: three failing v4 runs resumed and asked; all said "the skill should have said X", and v5 adds what they asked for
- [x] Re-test until no new rationalizations (v7)

## Quality
- [x] No flowchart: the decision is a first-match table
- [x] Quick reference table: the Decision table
- [x] Common mistakes: the Red flags list covers them
- [x] No narrative storytelling
- [x] Supporting files: none shipped with the skill; evals stay out of the package
- [x] Word count checked: about 1,100 words, over the 500 target; recorded as a known limit

## Deployment
- [x] Commit (branch bug-triage-hardening-2)
