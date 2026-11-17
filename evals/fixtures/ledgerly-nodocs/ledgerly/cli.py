# ABOUTME: Command-line entry point for the accountant.
# ABOUTME: Prints the monthly report for a given year and month.
import argparse


def main(argv=None):
    p = argparse.ArgumentParser(description="Genrate the monthly ledgerly report.")
    p.add_argument("year", type=int)
    p.add_argument("month", type=int)
    return p.parse_args(argv)


if __name__ == "__main__":
    main()
