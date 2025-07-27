class VendingMachine:
    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}  # Dictionary to hold item details
        self.balance = 0  # Current balance in the vending machine

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :return: None
        """
        if item_name in self.inventory:
            # If item already exists, update its price and add to its quantity
            self.inventory[item_name]['price'] = price
            self.inventory[item_name]['quantity'] += quantity
        else:
            # Add new item to the inventory
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :return: The balance of the vending machine after the coins are inserted, float.
        """
        self.balance += amount  # Increase balance by the inserted amount
        return self.balance

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float, otherwise, returns False.
        """
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if item['quantity'] > 0:
                if self.balance >= item['price']:
                    # Deduct item price from balance and reduce item quantity
                    self.balance -= item['price']
                    item['quantity'] -= 1
                    return self.balance
                else:
                    print("Insufficient balance. Please insert more coins.")
                    return False
            else:
                print(f"{item_name} is out of stock.")
                return False
        else:
            print(f"{item_name} is not available in the vending machine.")
            return False

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        """
        if item_name in self.inventory:
            # Increase the quantity of the existing item
            self.inventory[item_name]['quantity'] += quantity
            return True
        else:
            print(f"{item_name} is not available in the vending machine.")
            return False

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        """
        if not self.inventory:
            print("The vending machine is empty.")
            return False
        else:
            items_list = []
            for item_name, details in self.inventory.items():
                items_list.append(f"{item_name}: ${details['price']} ({details['quantity']} available)")
            return "\n".join(items_list)