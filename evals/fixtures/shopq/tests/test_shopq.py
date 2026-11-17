# ABOUTME: Smoke tests for shopq.
# ABOUTME: Run with python3 -m unittest discover tests.
import unittest

from shopq.export import export_rows
from shopq.qty import parse_qty


class SmokeTest(unittest.TestCase):
    def test_parse_qty(self):
        self.assertEqual(parse_qty("3"), 3)

    def test_export_header(self):
        self.assertTrue(export_rows([]).startswith("customer,sku,qty,total"))


if __name__ == "__main__":
    unittest.main()
