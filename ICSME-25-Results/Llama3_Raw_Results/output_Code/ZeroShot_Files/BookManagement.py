class BookManagement:
    def __init__(self):
        # Initialize an empty dictionary to store the inventory
        self.inventory = {}

    def add_book(self, title, quantity=1):
        # Check if the quantity is a positive integer
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid quantity. Quantity must be a positive integer.")
        
        # If the book is already in the inventory, increment its quantity
        if title in self.inventory:
            self.inventory[title] += quantity
        # If the book is not in the inventory, add it with the given quantity
        else:
            self.inventory[title] = quantity

        # Sort the inventory by book title
        self.inventory = dict(sorted(self.inventory.items()))

    def remove_book(self, title, quantity):
        # Check if the quantity is a positive integer
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid quantity. Quantity must be a positive integer.")
        
        # Check if the book is in the inventory
        if title not in self.inventory:
            raise ValueError("Book not found in inventory.")
        
        # Check if the quantity to remove is not more than the available quantity
        if quantity > self.inventory[title]:
            raise ValueError("Not enough quantity to remove.")
        
        # Decrement the quantity of the book
        self.inventory[title] -= quantity
        
        # If the quantity of the book becomes zero, remove it from the inventory
        if self.inventory[title] == 0:
            del self.inventory[title]

    def view_inventory(self):
        # Return the current inventory
        return self.inventory

    def view_book_quantity(self, title):
        # Return the quantity of the book if it exists in the inventory, otherwise return 0
        return self.inventory.get(title, 0)