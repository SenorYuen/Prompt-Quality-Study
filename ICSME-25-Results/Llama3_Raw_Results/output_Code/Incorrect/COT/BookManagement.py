class BookManagement:
    # Constructor to initialize the inventory
    def __init__(self):
        # Initialize an empty dictionary to store the inventory
        self.inventory = {}

    # Method to add one or several books to the inventory
    def add_book(self, title, quantity=1):
        # Check if the title already exists in the inventory
        if title in self.inventory:
            # If it exists, increment the quantity
            self.inventory[title] += quantity
        else:
            # If it does not exist, add it to the inventory with the given quantity
            self.inventory[title] = quantity
        # Sort the inventory by title
        self.inventory = dict(sorted(self.inventory.items()))

    # Method to remove one or several books from the inventory
    def remove_book(self, title, quantity):
        # Check if the title exists in the inventory
        if title in self.inventory:
            # Check if the quantity to remove is less than or equal to the available quantity
            if quantity <= self.inventory[title]:
                # If it is, decrement the quantity
                self.inventory[title] -= quantity
                # If the quantity reaches zero, remove the book from the inventory
                if self.inventory[title] == 0:
                    del self.inventory[title]
                return True
            else:
                # If the quantity to remove is more than the available quantity, return False
                return False
        else:
            # If the title does not exist in the inventory, return False
            return False

    # Method to get the inventory of the Book Management
    def view_inventory(self):
        # Return the current inventory
        return self.inventory

    # Method to get the quantity of a book
    def view_book_quantity(self, title):
        # Check if the title exists in the inventory
        if title in self.inventory:
            # If it exists, return the quantity
            return self.inventory[title]
        else:
            # If it does not exist, return 0
            return 0