# ------------------------------------------------------------
# CRUD en Python
# ------------------------------------------------------------
# Name: Jorge Orlando González Cárdenas
# Student ID: 2530260
# Group: IM 1-3
# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# This program implements a complete CRUD system (Create, Read,
# Update and Delete) using Python functions and an in-memory data
# structure. For storing items, I selected a dictionary where each
# key represents an item_id and each value is another dictionary
# containing the item fields. Using functions greatly improves
# organization because each operation is isolated, reusable, and
# easier to maintain. The program includes a text-based menu that
# allows the user to interact with the CRUD, perform validations,
# and manage items clearly and safely.
# ------------------------------------------------------------
# GOOD PRACTICES AND PRINCIPLES (STRINGS)
# ------------------------------------------------------------
# - Strings are immutable: any modification creates a new string.
# - Always normalize input with strip() and lower() before comparing it.
# - Avoid magic numbers when slicing; document each slice clearly.
# - Prefer built-in string methods instead of rewriting basic logic.
# - Validation order matters: first check empty input, then structure.
# - Write clean code with descriptive variable names and clear messages.
# - Use f-strings for readable and efficient string formatting.
# ------------------------------------------------------------
# Problem: In-memory CRUD manager with functions
# ------------------------------------------------------------
# Description:
# Program that implements a simple CRUD system (Create, Read,
# Update, Delete) for items stored in a dictionary and/or list.
# Each CRUD operation is handled by its own function, and the user
# interacts with the system through a text-based menu.
#
# Inputs:
# - Menu options selected by the user (string or int)
# - For CREATE/UPDATE: item_id, name, price, quantity
# - For READ/DELETE: item_id
#
# Outputs:
# - Messages indicating the result of each operation, such as:
#   "Item created", "Item updated", "Item deleted",
#   "Item not found", "Items list:", etc.
#
# Validations:
# - Menu option must be valid (for example, 0..4 or 0..5)
# - item_id must not be an empty string
# - Numeric fields (price, quantity) must be valid numbers >= 0
# - Prevent creating items using an existing item_id
# - For READ/UPDATE/DELETE: if item_id does not exist,
#   display "Item not found"
#
# Test cases:
# 1) Normal:
#    Actions: create an item, read it, update it, delete it
#    Expected: correct confirmation messages and final empty state
#
# 2) Border:
#    - Create an item with minimal valid data (quantity = 0)
#    - Use a very short or long item_id (if rules allow)
#    Expected: valid creation as long as validations are met
#
# 3) Error:
#    - Use invalid menu option (e.g., "9" or "x")
#    - Try to create an item with empty id
#    - Insert non-numeric values for price or quantity
#    Expected: "Error: invalid input" or corresponding error message
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

def create_item(items, item_id, name, price, quantity):
    """Creates a new item if item_id does not already exist."""
    if item_id in items:
        return False  # Duplicate ID not allowed
    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(items, item_id):
    """Returns the item dictionary if found, otherwise None."""
    return items.get(item_id)


def update_item(items, item_id, new_name, new_price, new_quantity):
    """Updates an existing item. Returns True if successful."""
    if item_id not in items:
        return False
    items[item_id]["name"] = new_name
    items[item_id]["price"] = new_price
    items[item_id]["quantity"] = new_quantity
    return True


def delete_item(items, item_id):
    """Deletes an item by id. Returns True if successful."""
    if item_id not in items:
        return False
    del items[item_id] 
    return True


def list_items(items):
    """Prints all items in a readable format."""
    if not items:
        print("No items available.")
        return
    print("Items list:")
    for item_id, data in items.items():
        print(f"- ID: {item_id}, Name: {data['name']}, Price: {data['price']}, Quantity: {data['quantity']}")

def main():
    items = {}  # Main data structure

    while True:
        print("\n----- MENU -----")
        print("1) Create item")
        print("2) Read item by ID")
        print("3) Update item by ID")
        print("4) Delete item by ID")
        print("5) List all items")
        print("0) Exit")

        option = input("Choose an option: ").strip()

        # Validate menu option
        if option not in ["0", "1", "2", "3", "4", "5"]:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        # CREATE 
        if option == "1":
            item_id = input("Enter item ID: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue

            name = input("Enter item name: ").strip()
            if name == "":
                print("Error: invalid input")
                continue

            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                if price < 0 or quantity < 0:
                    print("Error: invalid input")
                    continue
            except:
                print("Error: invalid input")
                continue

            if create_item(items, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: item ID already exists")

        # READ 
        elif option == "2":
            item_id = input("Enter item ID to read: ").strip()
            item = read_item(items, item_id)
            if item:
                print(f"Item found: Name = {item['name']}, Price = {item['price']}, Quantity = {item['quantity']}")
            else:
                print("Item not found")

        # UPDATE 
        elif option == "3":
            item_id = input("Enter item ID to update: ").strip()
            if item_id not in items:
                print("Item not found")
                continue

            new_name = input("Enter new name: ").strip()
            if new_name == "":
                print("Error: invalid input")
                continue

            try:
                new_price = float(input("Enter new price: "))
                new_quantity = int(input("Enter new quantity: "))
                if new_price < 0 or new_quantity < 0:
                    print("Error: invalid input")
                    continue
            except:
                print("Error: invalid input")
                continue

            if update_item(items, item_id, new_name, new_price, new_quantity):
                print("Item updated")
            else:
                print("Item not found")

        # DELETE 
        elif option == "4":
            item_id = input("Enter item ID to delete: ").strip()
            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        # LIST
        elif option == "5":
            list_items(items)


# Run the program
if __name__ == "__main__":
    main()
# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# Using functions for the CRUD operations helped keep the code organized,
# especially because each task (create, read, update, delete) is clearly
# separated and easier to maintain. Having a main menu loop that only
# calls these functions made the program cleaner and reduced repetition.
# This modular structure can be reused in larger systems such as inventory
# apps, student databases, or any program that stores and edits records.
# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python Official Documentation – Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 2) Python Official Documentation – Functions
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 3) Real Python – Dictionaries in Python
#    https://realpython.com/python-dicts/
#
# 4) W3Schools – Python Functions Tutorial
#    https://www.w3schools.com/python/python_functions.asp
#
# 5) Programiz – Python Dictionary (Beginner Guide)
#    https://www.programiz.com/python-programming/dictionary
# ------------------------------------------------------------
# END OF CODE
# ------------------------------------------------------------