class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item]['quantity'] > quantity:
                self.items[item]['quantity'] -= quantity
            else:
                del self.items[item]

    def view_items(self) -> dict:
        return self.items

    def total_price(self) -> float:
        total = 0.0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total