class Order:
    def __init__(self):
        # Initialize the order management system
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        # Check if the dish exists in the menu
        for menu_item in self.menu:
            if menu_item["dish"] == dish["dish"] and menu_item["price"] == dish["price"]:
                # Check if the count is valid
                if menu_item["count"] >= dish["count"]:
                    # Add the dish to the selected dishes
                    self.selected_dishes.append(dish)
                    # Update the count in the menu
                    menu_item["count"] -= dish["count"]
                    return True
        return False

    def calculate_total(self):
        # Initialize the total price
        total = 0
        # Calculate the total price of the selected dishes
        for dish in self.selected_dishes:
            # Check if the dish has a sales discount
            if dish["dish"] in self.sales:
                total += dish["price"] * dish["count"] * self.sales[dish["dish"]]
            else:
                total += dish["price"] * dish["count"]
        return total

    def checkout(self):
        # Check if there are selected dishes
        if self.selected_dishes:
            # Calculate the total price and return it
            return self.calculate_total()
        else:
            # Return False if there are no selected dishes
            return False