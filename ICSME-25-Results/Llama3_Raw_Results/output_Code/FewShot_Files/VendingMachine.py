class VendingMachine:
    """
    This is a class to simulate a vending machine, including adding products, inserting coins, purchasing products, viewing balance, replenishing product inventory, and displaying product information.
    """

    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}  # dictionary to store products and their details
        self.balance = 0  # initial balance of the vending machine

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :param item_name: The name of the product to be added, str.
        :param price: The price of the product to be added, float.
        :param quantity: The quantity of the product to be added, int.
        :return: None
        """
        # add product to inventory with its price and quantity
        self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted, float.
        :return: The balance of the vending machine after the coins are inserted, float.
        """
        # update the balance by adding the inserted amount
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
        :param item_name: The name of the product to be purchased, str.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float, otherwise, returns False.
        """
        # check if the product is available in the inventory
        if item_name in self.inventory:
            # check if the product is in stock
            if self.inventory[item_name]['quantity'] > 0:
                # check if the balance is sufficient to purchase the product
                if self.balance >= self.inventory[item_name]['price']:
                    # update the balance by subtracting the product's price
                    self.balance -= self.inventory[item_name]['price']
                    # update the product's quantity
                    self.inventory[item_name]['quantity'] -= 1
                    return self.balance
                else:
                    # not enough balance to purchase the product
                    return False
            else:
                # product is out of stock
                return False
        else:
            # product is not available in the inventory
            return False

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished, str.
        :param quantity: The quantity of the product to be replenished, int.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        """
        # check if the product is already in the inventory
        if item_name in self.inventory:
            # update the product's quantity
            self.inventory[item_name]['quantity'] += quantity
            return True
        else:
            # product is not available in the inventory
            return False

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        """
        # check if the vending machine is empty
        if not self.inventory:
            return False
        else:
            # create a string to display the products
            items_string = ''
            for item in self.inventory:
                items_string += f"{item} - ${self.inventory[item]['price']} [{self.inventory[item]['quantity']}] "
            return items_string