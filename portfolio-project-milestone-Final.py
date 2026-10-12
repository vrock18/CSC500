# Phase 1 Class Structures
# Class ItemToPurchase
class ItemToPurchase:
    # Default Constructor
    # Attributes(name, price, quantity, and description)
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    # I added setters so the values are checked before they are saved.
    # A price or quantity less than 0 will not work.
    # The name is saved in lower case to avoid errors due to case. 
    def set_item_name(self, name):
        self.item_name = name.lower()

    def set_item_description(self, description):
        self.item_description = description

    def set_item_price(self, price):
        if price < 0:
            print("Price cannot be negative. Price was not changed.")
        else:
            self.item_price = price

    def set_item_quantity(self, quantity):
        if quantity < 0:
            print("Quantity cannot be negative. Quantity was not changed.")
        else:
            self.item_quantity = quantity

    # Method: print_item_cost
    # Shows the item name, quantity, price, and the total cost for that item.
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")


# Class ShoppingCart
class ShoppingCart:
    # Default Constructor
    # Attributes (customer_name, current_date, and cart_items)
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []

    # Method: add_item
    # Adds an ItemToPurchase object to the cart_items list.
    def add_item(self, item):
        self.cart_items.append(item)

    # Method: remove_item
    # Deletes the specified item and confirms that item has been removed from cart.
    def remove_item(self, item_name):
        present = False
        for item in self.cart_items:
            if item.item_name == item_name.lower():
                self.cart_items.remove(item)
                print(f"{item.item_name} has been removed from your shopping cart.")
                present = True
                break  # stops looking after the item is deleted
        if present == False:
            print("Item not found in shopping cart. Nothing removed.")

    # Method: item_exists
    # Confirms that the specified item is in the shopping cart.
    def item_exists(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name.lower():
                return True
        return False

    # Method: modify_item
    # Receives a temporary ItemToPurchase object and updates the specified item in the shopping cart.
    def modify_item(self, item):
        present = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                present = True
                if item.item_description != "none":
                    cart_item.set_item_description(item.item_description)
                if item.item_price != 0.0:
                    cart_item.set_item_price(item.item_price)
                if item.item_quantity != 0:
                    cart_item.set_item_quantity(item.item_quantity)
        if present == False:
            print("Item not found in cart. Nothing modified.")

    # Method: get_num_items_in_cart
    # Returns the amount of items in the shopping cart.
    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items = total_items + item.item_quantity
        return total_items

    # Method: get_cost_of_cart
    # Returns the cost of all items in the shopping cart.
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost = total_cost + (item.item_price * item.item_quantity)
        return total_cost

    # Method: print_total
    # Displays the whole cart, or prints "SHOPPING CART IS EMPTY".
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    # Method: print_descriptions
    # Displays the description of items in the shopping cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


# Error Handling
# The program does not crash if the user types letters instead of a number, it keeps asking until the input is valid.
def get_valid_price(prompt):
    while True:
        try:
            price = float(input(prompt))
            if price < 0:
                print("Please enter a price that is not negative.")
            else:
                return price
        except ValueError:
            print("Invalid input. Please enter a number for the price (example: 10.99).")


def get_valid_quantity(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity < 0:
                print("Please enter a quantity that is not negative.")
            else:
                return quantity
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Phase 3 The Interactive Menu (print_menu)
# The loop keeps running until the user chooses option "q"
def print_menu(cart):
    choice = ""

    while choice != "q":
        print()
        print("***Shopping Cart Menu***")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        # .lower() lets the user type either "A" or "a" so the program doesn't get confused by case differences
        choice = input("Choose an option:\n").lower()

        # Option a: Add item
        # Creates a new ItemToPurchase object with setters to fill it in
        if choice == "a":
            print("\n***ADD ITEM TO CART***")
            new_item = ItemToPurchase()
            new_item.set_item_name(input("Enter the item name:\n"))
            new_item.set_item_description(input("Enter the item description:\n"))
            new_item.set_item_price(get_valid_price("Enter the item price without $ sign:\n"))
            new_item.set_item_quantity(get_valid_quantity("Enter the item quantity:\n"))
            cart.add_item(new_item)
            print(f"{new_item.item_name} has been added to your shopping cart.")

        # Option r: Remove item
        elif choice == "r":
            print("\n***REMOVE ITEM FROM CART***")
            name = input("Enter the name of the item to remove (or type menu to go back to the menu):\n")
            # Keep asking until the name matches an item in the shopping cart.
            # Typing "menu" also ends the loop so the user can go back to the menu.
            while name.lower() != "menu" and cart.item_exists(name) == False:
                print("\nError: That item is not in your shopping cart. Please try again.")
                name = input("Enter the name of the item to remove (or type menu to go back to the main menu):\n")
            # If the user typed "menu", skip removing and show the main menu again.
            if name.lower() == "menu":
                print("Returning to the main menu.")
            else:
                cart.remove_item(name)

        # Option c: Change item quantity
        # Makes a temporary ItemToPurchase object to to change the quantity.
        elif choice == "c":
            print("\n***CHANGE ITEM QUANTITY***")
            name = input("Enter the item name (or type menu to go back to the menu):\n")
            # Keep asking until the name matches an item in the shopping cart.
            # Typing "menu" ends the loop so the user can go back to the menu.
            while name.lower() != "menu" and cart.item_exists(name) == False:
                print("\nError: That item is not in your shopping cart. Please try again.")
                name = input("Enter the item name (or type menu to go back to the menu):\n")
            if name.lower() == "menu":
                print("Returning to the menu.")
            else:
                temp_item = ItemToPurchase()
                temp_item.set_item_name(name)
                temp_item.set_item_quantity(get_valid_quantity("Enter the new quantity:\n"))
                # If quantity is not 0, modify it. If it is 0 go back to the menu.
                if temp_item.item_quantity != 0:
                    cart.modify_item(temp_item)
                    print(f"The quantity of {temp_item.item_name} has been changed to {temp_item.item_quantity}.")

        # Option i: Output descriptions
        elif choice == "i":
            print("\n***ITEMS DESCRIPTIONS***")
            cart.print_descriptions()

        # Option o: Output shopping cart
        elif choice == "o":
            print("\n***ITEMS IN SHOPPING CART***")
            cart.print_total()

        # Option q: Quit
        # Show a thank you message, then the loop ends because user selected "q"
        elif choice == "q":
            print()
            print("***Thank you for shopping with us!***\n")

        # If the user input is anything else, it is invalid, so the menu shows again
        else:
            print("Invalid input, please choose a valid option.")


# Phase 2: Setup
# Prompt for the user's name and date to start the ShoppingCart object
customer = input("Enter customer's name:\n")
date = input("Enter today's date (MM/DD/YYYY):\n")

my_cart = ShoppingCart()
my_cart.customer_name = customer
my_cart.current_date = date

print()
print(f"Customer name: {my_cart.customer_name}")
print(f"Today's date: {my_cart.current_date}")

print_menu(my_cart)