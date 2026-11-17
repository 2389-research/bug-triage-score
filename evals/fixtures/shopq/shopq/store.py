# ABOUTME: Persists kiosk orders to a JSON file.
# ABOUTME: The nightly export reads orders back from the same file.
import json


def save_orders(path, orders):
    with open(path, "w") as f:
        json.dump(orders, f)


def load_orders(path):
    with open(path) as f:
        return json.load(f)
