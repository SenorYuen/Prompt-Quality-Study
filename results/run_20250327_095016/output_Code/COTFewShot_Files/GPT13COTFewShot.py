class BookManagement:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title, quantity=1):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity):
        if title in self.inventory:
            if self.inventory[title] >= quantity:
                self.inventory[title] -= quantity
                if self.inventory[title] == 0:
                    del self.inventory[title]
                return True
            else:
                return False
        else:
            return False

    def view_inventory(self):
        return self.inventory

    def view_book_quantity(self, title):
        return self.inventory.get(title, 0)