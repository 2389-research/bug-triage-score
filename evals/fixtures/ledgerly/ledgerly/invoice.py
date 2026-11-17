# ABOUTME: Invoice math used on the invoice detail page.
# ABOUTME: Line items carry quantity and unit price in cents.


def invoice_total(lines):
    return sum(l["qty"] * l["unit_cents"] for l in lines)


def average_unit_cents(lines):
    return sum(l["unit_cents"] for l in lines) // len(lines)
