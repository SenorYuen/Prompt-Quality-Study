class ShoppingCart:
    def __init__(self):
        """
        Initialize the items representing the shopping list as an empty dictionary.
        Each key is an item name, and the value is another dictionary with 'price' and 'quantity'.
        """
        self.items = {}

    def add_item(self, item, price, quantity=1):
        """
        Add item information to the shopping list items, including price and quantity.
        If the item already exists, update its quantity and price.
        :param item: str, the name of the item
        :param price: float, the price of the item
        :param quantity: int, the quantity of the item to add (default is 1)
        :return: None
        """
        if item in self.items:
            # Update existing item's quantity and price
            self.items[item]['quantity'] += quantity
            self.items[item]['price'] = price
        else:
            # Add new item with its price and quantity
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        """
        Subtract the specified quantity of item from the shopping list items.
        If the quantity to remove is greater than or equal to the existing quantity, remove the item entirely.
        :param item: str, the name of the item
        :param quantity: int, the quantity of the item to remove (default is 1)
        :return: None
        """
        if item in self.items:
            if self.items[item]['quantity'] > quantity:
                # Reduce the quantity of the item
                self.items[item]['quantity'] -= quantity
            else:
                # Remove the item entirely if quantity is less than or equal to the existing quantity
                del self.items[item]

    def view_items(self) -> dict:
        """
        Return the current shopping list items.
        :return: dict, the current shopping list items
        """
        return self.items

    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list.
        This is the sum of each item's price multiplied by its quantity.
        :return: float, the total price of all items in the shopping list
        """
        total = 0.0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total