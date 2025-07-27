class ShoppingCart:
    """
    The class manages items, their prices, quantities, and allows to for add, remove, view items, and calculate the total price.
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
        :param quantity:int, The number of items, defaults to 1
        :return:None
        """
        # Check if the item already exists in the shopping list
        if item in self.items:
            # If the item exists, update its quantity
            self.items[item]["quantity"] += quantity
        else:
            # If the item does not exist, add it to the shopping list
            self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item, quantity=1):
        """
        Subtract the specified quantity of item from the shopping list items
        :param item:string, Item to be subtracted in quantity
        :param quantity:int, Quantity to be subtracted
        :return:None
        """
        # Check if the item exists in the shopping list
        if item in self.items:
            # If the item exists, subtract the specified quantity
            if self.items[item]["quantity"] <= quantity:
                # If the quantity to be subtracted is greater than or equal to the existing quantity, remove the item from the shopping list
                del self.items[item]
            else:
                # If the quantity to be subtracted is less than the existing quantity, update the quantity
                self.items[item]["quantity"] -= quantity
        else:
            # If the item does not exist, print an error message
            print("Item not found in the shopping list")

    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return:dict, the current shopping list items
        """
        # Return the shopping list items
        return self.items

    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        """
        # Initialize the total price to 0
        total = 0
        # Iterate over each item in the shopping list
        for item in self.items:
            # Calculate the total price of the current item
            item_total = self.items[item]["price"] * self.items[item]["quantity"]
            # Add the total price of the current item to the overall total price
            total += item_total
        # Return the total price
        return total