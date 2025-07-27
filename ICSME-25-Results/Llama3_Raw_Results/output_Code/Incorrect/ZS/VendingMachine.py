class VendingMachine:
    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        # Initialize an empty dictionary to store the inventory
        self.inventory = {}
        # Initialize the balance to 0
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :return: None
        """
        # Check if the item is already in the inventory
        if item_name in self.inventory:
            # If the item is already in the inventory, update its quantity
            self.inventory[item_name]['quantity'] += quantity
        else:
            # If the item is not in the inventory, add it
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :return: The balance of the vending machine after the coins are inserted, float.
        """
        # Add the inserted amount to the balance
        self.balance += amount
        # Return the updated balance
        return self.balance

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float, otherwise, returns False.
        """
        # Check if the item is in the inventory
        if item_name in self.inventory:
            # Check if the item is in stock
            if self.inventory[item_name]['quantity'] > 0:
                # Check if the balance is sufficient to purchase the item
                if self.balance >= self.inventory[item_name]['price']:
                    # Update the balance
                    self.balance -= self.inventory[item_name]['price']
                    # Update the quantity of the item
                    self.inventory[item_name]['quantity'] -= 1
                    # Return the updated balance
                    return self.balance
                else:
                    # If the balance is not sufficient, return False
                    return False
            else:
                # If the item is out of stock, return False
                return False
        else:
            # If the item is not in the inventory, return False
            return False

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        """
        # Check if the item is in the inventory
        if item_name in self.inventory:
            # Update the quantity of the item
            self.inventory[item_name]['quantity'] += quantity
            # Return True
            return True
        else:
            # If the item is not in the inventory, return False
            return False

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        """
        # Check if the vending machine is empty
        if not self.inventory:
            # If the vending machine is empty, return False
            return False
        else:
            # Initialize an empty list to store the products
            products = []
            # Iterate over the items in the inventory
            for item, values in self.inventory.items():
                # Append the product information to the list
                products.append(f"{item}: ${values['price']} - {values['quantity']} in stock")
            # Return the list of products
            return products

    def view_balance(self):
        """
        Displays the current balance of the vending machine.
        :return: The current balance of the vending machine, float.
        """
        # Return the current balance
        return self.balance


# Example usage:
vending_machine = VendingMachine()
vending_machine.add_item("Soda", 1.50, 10)
vending_machine.add_item("Chips", 2.00, 5)
print(vending_machine.display_items())
vending_machine.insert_coin(5.00)
print(vending_machine.view_balance())
print(vending_machine.purchase_item("Soda"))
print(vending_machine.view_balance())
print(vending_machine.restock_item("Chips", 5))
print(vending_machine.display_items())