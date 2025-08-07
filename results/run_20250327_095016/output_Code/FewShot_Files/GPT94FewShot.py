class VendingMachine:
    """
    This is a class to simulate a vending machine, including adding products, inserting coins, purchasing products, viewing balance, replenishing product inventory, and displaying product information.
    """

    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :param item_name: The name of the product to be added, str.
        :param price: The price of the product to be added, float.
        :param quantity: The quantity of the product to be added, int.
        :return: None
        """
        # Add the item to the inventory with its price and quantity
        self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted, float.
        :return: The balance of the vending machine after the coins are inserted, float.
        """
        # Increase the balance by the inserted amount
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine.
        :param item_name: The name of the product to be purchased, str.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float, otherwise, returns False.
        """
        # Check if the item is in the inventory
        if item_name in self.inventory:
            item = self.inventory[item_name]
            # Check if the item is in stock and if the balance is sufficient
            if item['quantity'] > 0 and self.balance >= item['price']:
                # Deduct the item price from the balance and decrease the item quantity
                self.balance -= item['price']
                item['quantity'] -= 1
                return self.balance
        # Return False if the purchase cannot be completed
        return False

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished, str.
        :param quantity: The quantity of the product to be replenished, int.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        """
        # Check if the item is in the inventory
        if item_name in self.inventory:
            # Increase the item quantity
            self.inventory[item_name]['quantity'] += quantity
            return True
        # Return False if the item is not in the inventory
        return False

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        """
        # Check if the inventory is empty
        if not self.inventory:
            return False
        # Create a list of item details
        display_list = []
        for item_name, details in self.inventory.items():
            display_list.append(f"{item_name} - ${details['price']} [{details['quantity']}]")
        # Return the list of items as a string
        return ', '.join(display_list)