'''
# The class manages items, their prices, quantities, and allows to for add, removie, view items, and calculate the total price.

class ShoppingCart:
    def __init__(self):
        """
        Initialize the items representing the shopping list as an empty dictionary
        """


    def add_item(self, item, price, quantity=1):
        """
        Add item information to the shopping list items, including price and quantity. The default quantity is 1
        :return:None
        """


    def remove_item(self, item, quantity=1):
        """
        Subtract the specified quantity of item from the shopping list items
        :return:None
        """


    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return:dict, the current shopping list items
        """


    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        """

'''



class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item] = {'price': price, 'quantity': quantity}
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] -= quantity
        else:
            pass

    def view_items(self) -> dict:
        return self.items

    def total_price(self) -> float:
        return sum([item['quantity'] * item['price'] for item in self.items.values()])

