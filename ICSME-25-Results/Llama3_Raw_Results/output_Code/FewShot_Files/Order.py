class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of resturant inventory
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dished selected by customer
        selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales stores the sales of each dish
        sales = {dish name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        """
        # Check if the dish exists in the menu
        for menu_item in self.menu:
            if menu_item["dish"] == dish["dish"] and menu_item["price"] == dish["price"]:
                # Check if the count is valid
                if menu_item["count"] >= dish["count"]:
                    # Add the dish to the selected dishes
                    self.selected_dishes.append({"dish": dish["dish"], "count": dish["count"], "price": dish["price"]})
                    # Update the count in the menu
                    menu_item["count"] -= dish["count"]
                    return True
        return False

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """
        # Initialize the total
        total = 0
        # Iterate over the selected dishes
        for dish in self.selected_dishes:
            # Check if the dish has a sales value
            if dish["dish"] in self.sales:
                # Calculate the total price with sales
                total += dish["count"] * dish["price"] * self.sales[dish["dish"]]
            else:
                # Calculate the total price without sales
                total += dish["count"] * dish["price"]
        return total

    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        """
        # Check if there are selected dishes
        if self.selected_dishes:
            # Calculate and return the total
            return self.calculate_total()
        else:
            # Return False if there are no selected dishes
            return False