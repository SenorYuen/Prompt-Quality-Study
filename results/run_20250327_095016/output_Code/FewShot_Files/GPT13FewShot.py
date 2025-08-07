class BookManagement:
    """
    This is a class for managing a book system, which supports adding and removing books from the inventory dict, viewing the inventory, and checking the quantity of a specific book.
    """

    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise an error if the input is invalid.
        :param title: str, the book title
        :param quantity: int
        """
        if title in self.inventory:
            if self.inventory[title] >= quantity:
                self.inventory[title] -= quantity
                if self.inventory[title] == 0:
                    del self.inventory[title]
            else:
                raise ValueError("Cannot remove more books than are available in inventory.")
        else:
            raise KeyError("Book title not found in inventory.")

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        """
        return self.inventory

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.inventory
        """
        return self.inventory.get(title, 0)