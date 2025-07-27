class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item]["quantity"] <= quantity:
                del self.items[item]
            else:
                self.items[item]["quantity"] -= quantity

    def view_items(self):
        return self.items

    def total_price(self):
        total = 0
        for item in self.items:
            total += self.items[item]["price"] * self.items[item]["quantity"]
        return total