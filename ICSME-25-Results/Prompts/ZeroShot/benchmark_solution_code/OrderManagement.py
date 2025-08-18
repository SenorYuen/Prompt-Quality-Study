'''
# The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.

class Order:

    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of resturant inventory
        """


    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :return: True if successfully added, or False otherwise.
        """

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """

    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        """
        
'''

class Order:

    def __init__(self):
        self.menu = []
        # menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes = []
        # selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales = {}
        # 


    def add_dish(self, dish):
        for menu_dish in self.menu:
            if dish["dish"] == menu_dish["dish"]:
                if menu_dish["count"] < dish["count"]:
                    return False
                else:
                    menu_dish["count"] -= dish["count"]
                    break
        self.selected_dishes.append(dish)
        return True

    def calculate_total(self):
        total = 0
        for dish in self.selected_dishes:
            total += dish["price"] * dish["count"] * self.sales[dish["dish"]]
        return total

    def checkout(self):
        if len(self.selected_dishes) == 0:
            return False
        total = self.calculate_total()
        self.selected_dishes = []
        return total
