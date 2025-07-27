class VendingMachine:
    def __init__(self):
        self.inventory = {}
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        if item_name in self.inventory and self.inventory[item_name]['quantity'] > 0:
            if self.balance >= self.inventory[item_name]['price']:
                self.balance -= self.inventory[item_name]['price']
                self.inventory[item_name]['quantity'] -= 1
                return self.balance
        return False

    def restock_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        return False

    def display_items(self):
        if not self.inventory:
            return False
        return [f"{item} - ${info['price']} [{info['quantity']}]" for item, info in self.inventory.items()]