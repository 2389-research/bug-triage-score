# ABOUTME: Builds the monthly per-category report for the accountant.
# ABOUTME: Transactions carry UTC datetimes and amounts in cents.
from collections import defaultdict


def monthly_totals(transactions, year, month):
    totals = defaultdict(int)
    for t in transactions:
        ts = t["timestamp"]
        if ts.year == year and ts.month == month:
            totals[t["category"]] += t["cents"]
    return dict(sorted(totals.items()))
