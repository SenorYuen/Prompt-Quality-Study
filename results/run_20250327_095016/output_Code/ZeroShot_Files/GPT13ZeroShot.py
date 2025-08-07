class BookManagement:
    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        self.inventory = {}  # Dictionary to hold book titles and their quantities

    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        """
        if title in self.inventory:
            self.inventory[title] += quantity  # Increase quantity if book already exists
        else:
            self.inventory[title] = quantity  # Add new book with specified quantity

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise False while get invalid input.
        """
        if title in self.inventory:
            if self.inventory[title] >= quantity:
                self.inventory[title] -= quantity  # Decrease quantity if sufficient stock exists
                if self.inventory[title] == 0:
                    del self.inventory[title]  # Remove book from inventory if quantity is zero
            else:
                raise ValueError("Not enough books in inventory to remove the specified quantity.")  # Raise error if insufficient stock
        else:
            raise ValueError("Book not found in inventory.")  # Raise error if book does not exist

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        """
        return self.inventory  # Return the entire inventory dictionary

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.inventory
        """
        return self.inventory.get(title, 0)  # Return quantity if book exists, otherwise return 0