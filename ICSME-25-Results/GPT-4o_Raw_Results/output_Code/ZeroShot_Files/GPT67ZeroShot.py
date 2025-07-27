class Order:

    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of restaurant inventory
        """
        # Sample menu with dish names as keys and a tuple of (price, count) as values
        self.menu = {
            "Pasta": (10.0, 5),
            "Pizza": (12.0, 3),
            "Salad": (8.0, 10)
        }
        # Initialize selected_dishes to store ordered dishes and their counts
        self.selected_dishes = {}

    def add_dish(self, dish, count):
        """
        Check the self.menu and add into self.selected_dishes if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: str, name of the dish
        :param count: int, number of dishes to add
        :return: True if successfully added, or False otherwise.
        """
        if dish in self.menu and self.menu[dish][1] >= count:
            # Add dish to selected_dishes or update the count if it already exists
            if dish in self.selected_dishes:
                self.selected_dishes[dish] += count
            else:
                self.selected_dishes[dish] = count
            # Decrease the count in the menu
            self.menu[dish] = (self.menu[dish][0], self.menu[dish][1] - count)
            return True
        return False

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """
        total = 0.0
        for dish, count in self.selected_dishes.items():
            price = self.menu[dish][0]
            total += price * count
        return total

    def checkout(self):
        """
        Check out the dishes ordered. If the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return: False if the self.selected_dishes is empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        return self.calculate_total()