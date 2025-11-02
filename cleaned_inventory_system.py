"""Inventory System - A simple demo for static code analysis lab."""
import json
import logging
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add quantity of an item to the inventory."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.basicConfig(level=logging.INFO)
    logging.info("Item added successfully")


def remove_item(item, qty):
    """Delete quantity of an item to the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")


def get_qty(item):
    """Get quantity of an item to the inventory."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load Data into a json file."""
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        stock_data.clear()
        stock_data.update(data)


def save_data(file="inventory.json"):
    """Save Data into a json file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print Data."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Check which all have low items in inventory."""
    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """Main function to test inventory system functionality."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


main()
