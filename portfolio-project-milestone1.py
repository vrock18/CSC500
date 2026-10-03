# input() always gives us back a string, so we use float() for money to consider cents and use int() for quantity since this will be whole numbers.

# --- Variables needed for the ShoppingCart part of the final app ---
customer_name = input("Enter the customer name: ")
current_date = input("Enter today's date: ")

# input() always gives us back a string, and that works fine for item_name and item_description, so I use float() for item_price to consider cents and use int() for quantity since this will be whole numbers.
item_name = input("Enter the item name: ")
item_description = input("Enter the item description: ")
item_price = float(input("Enter the item price: "))
item_quantity = int(input("Enter the item quantity: "))

# Arithmetic Expression 1: subtotal = price * quantity
subtotal = item_price * item_quantity

# Arithmetic Expression 2: total with sales tax added (8.5% tax rate)
tax_rate = 0.085
total_with_tax = subtotal + (subtotal * tax_rate)


# To use + to join strings together, everything has to be a string.
# round(number, 2) rounds to 2 decimal places, so the money looks like cashe ona  real life transaction.
print()
print("----- Receipt -----")
print("Customer: " + customer_name)
print("Date: " + current_date)
print("Item: " + item_name)
print("Description: " + item_description)
print("Price: $" + str(item_price))
print("Quantity: " + str(item_quantity))
print("Subtotal: $" + str(round(subtotal, 2)))
print("Total with tax: $" + str(round(total_with_tax, 2)))