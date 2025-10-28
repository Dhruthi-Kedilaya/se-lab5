"""
Inventory Management System
This module provides basic inventory management functions such as
adding, removing, and saving items, with logging support.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a specific quantity of an item to the stock."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info(f"Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specific quantity of an item from the stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        logging.warning(
            f"Attempted to remove item '{item}' that doesn't exist: {e}"
        )


def get_qty(item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.load(f)


def save_data(file="inventory.json"):
    """Save current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print all items and their quantities."""
    print("Items Report")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the specified threshold."""
    return [i for i, qty in stock_data.items() if qty < threshold]


def main():
    """Demonstrate the inventory system functions."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("123", 10)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("Eval removed: safe print instead of eval")


if __name__ == "__main__":
    main()
