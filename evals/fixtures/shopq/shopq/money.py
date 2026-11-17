# ABOUTME: Formats prices for receipts and the export.
# ABOUTME: Prices are stored as floats in dollars.


def format_price(amount):
    return f"${round(amount, 2):.2f}"
