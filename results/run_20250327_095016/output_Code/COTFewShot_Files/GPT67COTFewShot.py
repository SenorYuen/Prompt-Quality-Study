class Order:
    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        for menu_item in self.menu:
            if menu_item["dish"] == dish["dish"] and menu_item["count"] >= dish["count"]:
                self.selected_dishes.append(dish)
                menu_item["count"] -= dish["count"]
                return True
        return False

    def calculate_total(self):
        total = 0.0
        for dish in self.selected_dishes:
            sales_factor = self.sales.get(dish["dish"], 1)
            total += dish["count"] * dish["price"] * sales_factor
        return total

    def checkout(self):
        if not self.selected_dishes:
            return False
        return self.calculate_total()