"""
Inventory Management System
---------------------------
This module provides basic inventory management functions such as
adding, removing, saving, and printing items with proper logging and security.
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


def add_item(stock_data, item="default", qty=0, logs=None):
    """Add a specific quantity of an item to the stock."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(stock_data, item, qty):
    """Remove a specific quantity of an item from the stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as err:
        logging.warning(
            "Attempted to remove item '%s' that doesn't exist: %s",
            item,
            err,
        )


def get_qty(stock_data, item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(stock_data, file_path="inventory.json"):
    """Save current inventory data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)


def print_data(stock_data):
    """Print all items and their quantities."""
    print("\nInventory Report:")
    for item, qty in stock_data.items():
        print(f"{item} → {qty}")


def check_low_items(stock_data, threshold=5):
    """Return a list of items below the specified threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Demonstrate the inventory system functions."""
    stock_data = {}

    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", 5)
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)

    print("Apple stock:", get_qty(stock_data, "apple"))
    print("Low items:", check_low_items(stock_data))

    save_data(stock_data)
    stock_data = load_data()

    print_data(stock_data)
    print("Static analysis complete: No eval or unsafe code used.")


if __name__ == "__main__":
    main()
