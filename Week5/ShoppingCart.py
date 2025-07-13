# Added a cancel option to the shopping cart program

# Global variables to store cart data
items = []
prices = []
currency_symbol = "$"

def add_item():
    # Add an item with its price to the shopping cart
    item_name = input("What item would you like to add? (Leave blank to cancel): ")

    if not item_name.strip():
        print("Item addition cancelled.")
        print()
        return

    while True:
        try:
            price = float(input(f"What is the price of '{item_name}'? "))
            break
        except ValueError:
            print("Please enter a valid price (number).")
            print()

    items.append(item_name)
    prices.append(price)
    print(f"'{item_name}' has been added to the cart.")
    print()

def display_items():
    # Display all items in the cart with their prices and numbers
    if not items:
        print("Your shopping cart is empty.")
        print()
        return

    print("The contents of the shopping cart are:")
    for i in range(len(items)):
        print(f"{i + 1}. {items[i]} - {currency_symbol}{prices[i]:.2f}")

def remove_item():
    # Remove an item from the shopping cart
    if not items:
        print("Your shopping cart is empty. Nothing to remove.")
        print()
        return

    display_items()

    while True:
        try:
            item_number = int(input("Which item would you like to remove? (Enter the item number, or 0 to cancel): "))

            if item_number == 0:
                print("Item removal cancelled.")
                print()
                return

            # Convert to 0-based index
            index = item_number - 1

            # Check if index is within bounds
            if index < 0 or index >= len(items):
                print(f"Invalid item number. Please enter a number between 1 and {len(items)}.")
                print()
                continue

            # Remove item and price
            items.pop(index)
            prices.pop(index)

            print("Item removed.")
            print()
            break

        except ValueError:
            print("Please enter a valid number.")
            print()

def calculate_total():
    # Calculate and display the total price of all items
    if not items:
        print("Your shopping cart is empty. Total: $0.00")
        print()
        return

    total = sum(prices)
    print(f"The total price of the items in the shopping cart is {currency_symbol}{total:.2f}")
    print()

print("Welcome to the Shopping Cart Program!")

while True:
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print()

    choice = input("Please enter an action: ")

    # Process the user's menu choice and return True to continue, False to exit
    if choice == "1":
        add_item()
    elif choice == "2":
        display_items()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        calculate_total()
    elif choice == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        print()
