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
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] > 0:
                if self.balance >= self.inventory[item_name]['price']:
                    self.balance -= self.inventory[item_name]['price']
                    self.inventory[item_name]['quantity'] -= 1
                    return self.balance
                else:
                    return False
            else:
                return False
        else:
            return False

    def restock_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        else:
            return False

    def display_items(self):
        if self.inventory:
            items = []
            for item in self.inventory:
                items.append(f'{item} - ${self.inventory[item]["price"]} [{self.inventory[item]["quantity"]}]')
            return items
        else:
            return False