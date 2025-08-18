'''
# This is a class as managing books system, which supports to add and remove books from the inventory dict, view the inventory, and check the quantity of a specific book.

class BookManagement:
    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """

    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        """

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        """

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        """

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.inventory
        """
'''


class BookManagement:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title, quantity=1):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity):
        if title not in self.inventory or self.inventory[title] < quantity:
            raise False
        self.inventory[title] -= quantity
        if self.inventory[title] == 0:
            del (self.inventory[title])

    def view_inventory(self):
        return self.inventory

    def view_book_quantity(self, title):
        if title not in self.inventory:
            return 0
        return self.inventory[title]


