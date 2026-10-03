# Step 1: Build the ItemToPurchase Class
class ItemToPurchase:
    # Default Constructor
    # Attributes and I added the item_description attribute
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"
 
    # Method:
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
 
# Steps 2 and 3 were removed since the ShoppingCart class and the menu now handle adding items and showing the total cost.

# Step 4: Build the ShoppingCart Class
class ShoppingCart:
    # Default Constructor
    # Attributes
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []
 
    # Core Method: add_item
    # ItemToPurchase adds object to the list
    def add_item(self, item):
        self.cart_items.append(item)
 
    # Core Method: remove_item
    # Removes an item by name; if not found, output: Item not found in cart. Nothing removed.
    def remove_item(self, item_name):
        present = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                present = True
                break  # stops looking after deleting item
        if present == False:
            print("Item not found in cart. Nothing removed.")
 
    # Core Method: modify_item
    # Updates an item if already is in the cart
    def modify_item(self, item):
        present = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                present = True
                # Changes values that were inputted
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0.0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
        if present == False:
            print("Item not found in your shopping cart. Nothing changed.")
 
    # Core Method: get_num_items_in_cart
    # Returns the total quantity of all items
    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items = total_items + item.item_quantity
        return total_items
 
    # Core Method: get_cost_of_cart
    # Returns the total cost of all items
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost = total_cost + (item.item_price * item.item_quantity)
        return total_cost
 
    # Core Method: print_total
    # Displays the full cart, or SHOPPING CART IS EMPTY
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
        print(f"Total: ${self.get_cost_of_cart()}")
 
    # Core Method: print_descriptions
    # Displays the description of every item in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")
 
 
# Step 5 & 6: The User Interface (print_menu)
def print_menu(cart):
    choice = ""
 
    # Loop that keeps going until q is selected
    while choice != "q":
        # Menu options
        print()
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from shopping cart")
        print("c - Change item quantity in shopping cart")
        print("i - Output descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()
 
        # Ask the user to choose an option
        choice = input("Choose an option:\n")
 
        # Option a: Add item
        if choice == "a":
            print("\n***ADD NEW ITEM TO YOUR SHOPPING CART***")
            new_item = ItemToPurchase()
            new_item.item_name = input("Enter the item name:\n")
            new_item.item_description = input("Enter the item description:\n")
            new_item.item_price = float(input("Enter the item price without $ sign:\n"))
            new_item.item_quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(new_item)
 
        # Option r: Remove item
        elif choice == "r":
            print("\n***REMOVE AN ITEM FROM YOUR SHOPPING CART***")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
 
        # Option c: Change quantity
        elif choice == "c":
            print("\n***CHANGE THE QUANTITY OF AN ITEM IN YOUR SHOPPING CART***")
            changed_item = ItemToPurchase()
            changed_item.item_name = input("Enter the item name:\n")
            changed_item.item_quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(changed_item)
 
        # Option i: Output descriptions
        elif choice == "i":
            print("\n***VIEW THE DESCRIPTIONS OF ITEMS IN YOUR SHOPPING CART***")
            cart.print_descriptions()
 
        # Option o: Output shopping cart
        elif choice == "o":
            print("\n***VIEW SHOPPING CART***")
            cart.print_total()
 
        # Option q: Quit
        # Anything else (except q) is invalid, so the loop shows the user the menu again
        # I chose to have the menu show again after an invalid selection so the user can see all of the options again before choosing.
        elif choice != "q":
            print("Invalid input, please choose a valid option.")
 
 
# Prompts to start the Program
customer = input("Enter customer's name:\n")
date = input("Enter today's date:\n")

# Create the cart, and start the menu
my_cart = ShoppingCart()
my_cart.customer_name = customer
my_cart.current_date = date
 
print()
print(f"Customer name: {my_cart.customer_name}")
print(f"Today's date: {my_cart.current_date}")
 
print_menu(my_cart)