# ABOUTME: Smoke tests for ledgerly.
# ABOUTME: Run with python3 -m unittest discover tests.
import unittest
from datetime import datetime, timezone

from ledgerly.invoice import invoice_total
from ledgerly.report import monthly_totals


class SmokeTest(unittest.TestCase):
    def test_invoice_total(self):
        self.assertEqual(invoice_total([{"qty": 2, "unit_cents": 150}]), 300)

    def test_monthly_totals(self):
        t = {"timestamp": datetime(2026, 3, 10, 15, tzinfo=timezone.utc), "category": "rent", "cents": 100}
        self.assertEqual(monthly_totals([t], 2026, 3), {"rent": 100})


if __name__ == "__main__":
    unittest.main()
