class ShoppingCart:
    """
    The class manages items, their prices, quantities, and allows for adding, removing, viewing items, and calculating the total price.
    """

    def __init__(self):
        """
        Initialize the items representing the shopping list as an empty dictionary
        """
        self.items = {}

    def add_item(self, item, price, quantity=1):
        """
        Add item information to the shopping list items, including price and quantity. The default quantity is 1
        :param item: string, Item to be added
        :param price: float, The price of the item
        :param quantity: int, The number of items, defaults to 1
        :return: None
        """
        if item in self.items:
            # If the item already exists, update the quantity
            self.items[item]['quantity'] += quantity
        else:
            # Add new item with price and quantity
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        """
        Subtract the specified quantity of item from the shopping list items
        :param item: string, Item to be subtracted in quantity
        :param quantity: int, Quantity to be subtracted
        :return: None
        """
        if item in self.items:
            if self.items[item]['quantity'] <= quantity:
                # If quantity to remove is greater or equal, remove the item completely
                del self.items[item]
            else:
                # Otherwise, just decrease the quantity
                self.items[item]['quantity'] -= quantity

    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return: dict, the current shopping list items
        """
        return self.items

    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return: float, the total price of all items in the shopping list
        """
        total = 0.0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total