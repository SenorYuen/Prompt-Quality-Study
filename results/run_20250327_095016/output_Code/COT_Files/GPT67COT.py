class Order:
    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        for item in self.menu:
            if item["dish"] == dish["dish"] and item["count"] >= dish["count"]:
                self.selected_dishes.append(dish)
                item["count"] -= dish["count"]
                return True
        return False

    def calculate_total(self):
        total = 0.0
        for dish in self.selected_dishes:
            price = dish["price"]
            count = dish["count"]
            sales_multiplier = self.sales.get(dish["dish"], 1)
            total += price * count * sales_multiplier
        return total

    def checkout(self):
        if not self.selected_dishes:
            return False
        total = self.calculate_total()
        self.selected_dishes.clear()
        return total