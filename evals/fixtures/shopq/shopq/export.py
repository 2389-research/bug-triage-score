# ABOUTME: Writes the nightly per-customer order export.
# ABOUTME: Output is a CSV the accounting team opens in a spreadsheet.
from shopq.money import format_price


def export_rows(orders):
    lines = ["customer,sku,qty,total"]
    for o in orders:
        total = format_price(o["qty"] * o["price"])
        lines.append(f"{o['customer']},{o['sku']},{o['qty']},{total}")
    return "\n".join(lines) + "\n"


def write_export(path, orders):
    with open(path, "w") as f:
        f.write(export_rows(orders))
