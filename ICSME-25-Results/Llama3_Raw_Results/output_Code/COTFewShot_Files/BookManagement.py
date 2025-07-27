class BookManagement:
    def __init__(self):
        # Initialize the inventory of the Book Manager
        self.inventory = {}

    def add_book(self, title, quantity=1):
        # Add one or several books to inventory which is sorted by book title
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity
        # Sort the inventory by book title
        self.inventory = dict(sorted(self.inventory.items()))

    def remove_book(self, title, quantity):
        # Remove one or several books from inventory
        if title in self.inventory:
            if self.inventory[title] >= quantity:
                self.inventory[title] -= quantity
                if self.inventory[title] == 0:
                    del self.inventory[title]
                return True
            else:
                return False
        else:
            return False

    def view_inventory(self):
        # Get the inventory of the Book Management
        return self.inventory

    def view_book_quantity(self, title):
        # Get the quantity of a book
        if title in self.inventory:
            return self.inventory[title]
        else:
            return 0