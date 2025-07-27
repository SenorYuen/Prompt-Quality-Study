class Order:
    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        # Check if the dish exists in the menu and if the count is valid
        for menu_dish in self.menu:
            if menu_dish["dish"] == dish["dish"] and menu_dish["count"] >= dish["count"]:
                # Update the count in the menu
                menu_dish["count"] -= dish["count"]
                # Add the dish to the selected dishes
                self.selected_dishes.append(dish)
                return True
        return False

    def calculate_total(self):
        total = 0
        # Calculate the total price of dishes
        for dish in self.selected_dishes:
            if dish["dish"] in self.sales:
                total += dish["count"] * dish["price"] * self.sales[dish["dish"]]
            else:
                total += dish["count"] * dish["price"]
        return total

    def checkout(self):
        if not self.selected_dishes:
            return False
        return self.calculate_total()