print("Welcome! This program will help you calculate the total cost for a group meal, including tax and change.")
print("Please enter all values carefully. Negative numbers and invalid inputs are not allowed.")

# Inputs
while True:
    child_meal_price = float(input("Enter the price of a child's meal: "))
    if child_meal_price >= 0:
        break
    print("Price cannot be negative. Please re-enter.")
while True:
    adult_meal_price = float(input("Enter the price of an adult's meal: "))
    if adult_meal_price >= 0:
        break
    print("Price cannot be negative. Please re-enter.")
while True:
    number_of_children = int(input("Enter the number of children: "))
    if number_of_children >= 0:
        break
    print("Number cannot be negative. Please re-enter.")
while True:
    number_of_adults = int(input("Enter the number of adults: "))
    if number_of_adults >= 0:
        break
    print("Number cannot be negative. Please re-enter.")

# Subtotal calculation
subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
print(f"Subtotal: ${subtotal:.2f}")

# Tax and total
while True:
    sales_tax_rate = float(input("Enter the sales tax rate (as a percentage): "))
    if sales_tax_rate >= 0:
        break
    print("Tax rate cannot be negative. Please re-enter.")
sales_tax = subtotal * (sales_tax_rate / 100)
total = subtotal + sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

# Payment and change
while True:
    payment_amount = float(input("Enter the payment amount: "))
    if payment_amount >= total:
        break
    print(f"Payment must be at least ${total:.2f}. Please re-enter.")
change = payment_amount - total
print(f"Change: ${change:.2f}")
