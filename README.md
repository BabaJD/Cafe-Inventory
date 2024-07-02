# Cafe-Inventory Value Calculator
A software solution in Python for efficient inventory management in a cafe

## Description

This Python script is designed to calculate the total monetary value of inventory items in a cafe setting. It utilizes dictionaries to store item names, stock quantities, and prices, then iterates through the inventory to compute the value of each item and the total value of all items combined.

**Key Features:**

* **Item Tracking:** Stores a list of cafe menu items (`menu_list`).
* **Inventory Management:** Maintains the current stock of each item in a dictionary (`stock`).
* **Price Listing:** Keeps track of the price of each item in a separate dictionary (`prices`).
* **Value Calculation:** Calculates the individual value of each item's stock and the total inventory value.
* **Output:** Provides a clear breakdown of the value for each item and the overall inventory value in a formatted string.

## Purpose

This script is a practical tool for cafe owners or managers. By understanding the value of their inventory, they can make informed decisions about:

* **Ordering:**  Knowing when to reorder items based on current stock levels and value.
* **Pricing:** Assessing whether prices are appropriate for the cost of inventory.
* **Profitability:** Analyzing the relationship between inventory costs and overall revenue.

## Usage

1. **Run the script:** Execute the Python script from your terminal or IDE.

2. **Output:** The script will print to the console:
    * The value of each item's stock in the format: "The value of the stock item for [item name] is $[value]".
    * The total value of the cafe's inventory: "The total value of the cafe's inventory is $[total value]".

## Customization (Optional)

You can easily adapt this script to your specific cafe:

* **Modify Lists and Dictionaries:** Update `menu_list`, `stock`, and `prices` with your cafe's actual items, quantities, and prices.
* **Enhance Output:** Format the output to your liking (e.g., add currency symbols, align columns).
* **Add Features:**  
    * Implement a way to read inventory data from a file (CSV, JSON).
    * Allow for user input to update stock levels or prices.
    * Calculate potential profits based on estimated sales.
    * Integrate with a database for persistent storage.

## Code Overview

* **Dictionaries:**  `stock` and `prices` use item names as keys to quickly retrieve quantities and prices.
* **Loops:** A `for` loop iterates through `menu_list`, fetching corresponding data from the dictionaries and calculating values.

## Credits

* **Author:** Babajide Abraham Alamu
