class BookManagement:
    """
    This is a class as managing books system, which supports to add and remove books from the inventory dict, view the inventory, and check the quantity of a specific book.
    """

    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        # Initialize an empty dictionary to store the inventory
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        # Check if the title already exists in the inventory
        if title in self.inventory:
            # If it exists, increment the quantity
            self.inventory[title] += quantity
        else:
            # If it doesn't exist, add it to the inventory with the given quantity
            self.inventory[title] = quantity
        # Sort the inventory by book title
        self.inventory = dict(sorted(self.inventory.items()))

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        # Check if the title exists in the inventory
        if title in self.inventory:
            # Check if the quantity to remove is valid (not more than the available quantity)
            if quantity <= self.inventory[title]:
                # If it's valid, decrement the quantity
                self.inventory[title] -= quantity
                # If the quantity reaches 0, remove the book from the inventory
                if self.inventory[title] == 0:
                    del self.inventory[title]
            else:
                # If it's not valid, raise a ValueError
                raise ValueError("Invalid quantity to remove")
        else:
            # If the title doesn't exist, raise a ValueError
            raise ValueError("Book not found in inventory")

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1}
        """
        # Return the current inventory
        return self.inventory

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.invenroty
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        0
        """
        # Check if the title exists in the inventory
        if title in self.inventory:
            # If it exists, return the quantity
            return self.inventory[title]
        else:
            # If it doesn't exist, return 0
            return 0