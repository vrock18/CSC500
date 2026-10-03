# Step 1: Build the ItemToPurchase Class
class ItemToPurchase:
    # Default Constructor
    # Attributes
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
 
    # Method:
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
 
 
# Step 2: Main Program Implementation
print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name:\n")
item1.item_price = float(input("Enter the item price without $ sign:\n"))
item1.item_quantity = int(input("Enter the item quantity:\n"))
 
print()  # Just blank space
 
print("Item 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name:\n")
item2.item_price = float(input("Enter the item price without $ sign:\n"))
item2.item_quantity = int(input("Enter the item quantity:\n"))
 
 # Step 3: Output the Total Cost
print()  # More blank space
print("TOTAL COST")
 
item1.print_item_cost()
item2.print_item_cost()
 
# Calculate the combined total cost of both items and display costs
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
 
print(f"Total: ${total_cost}")