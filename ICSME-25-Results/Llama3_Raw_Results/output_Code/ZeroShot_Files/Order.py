class Order:
    def __init__(self, menu=None):
        # Initialize the order management system
        # self.menu stores the dishes of restaurant inventory
        # self.selected_dishes stores the dishes that have been ordered
        self.menu = menu if menu else {}
        self.selected_dishes = {}

    def add_dish(self, dish, count=1):
        # Check the self.menu and add into self.selected_dish if the dish count is valid
        # And if the dish has successfully been added, change the count in self.menu
        # :return: True if successfully added, or False otherwise
        if dish in self.menu and self.menu[dish]['count'] >= count:
            if dish in self.selected_dishes:
                self.selected_dishes[dish]['count'] += count
            else:
                self.selected_dishes[dish] = {'price': self.menu[dish]['price'], 'sales': self.menu[dish]['sales'], 'count': count}
            self.menu[dish]['count'] -= count
            return True
        return False

    def calculate_total(self):
        # Calculate the total price of dishes that have been ordered
        # Multiply the count, price and sales
        # :return total: float, the final total price
        total = 0
        for dish, details in self.selected_dishes.items():
            total += details['count'] * details['price'] * (1 - details['sales'])
        return total

    def checkout(self):
        # Check out the dishes ordered
        # IF the self.selected_dishes is not empty, invoke the calculate_total method to check out
        # :return False if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise
        if not self.selected_dishes:
            return False
        return self.calculate_total()


# Example usage:
menu = {
    'dish1': {'price': 10.0, 'sales': 0.1, 'count': 10},
    'dish2': {'price': 20.0, 'sales': 0.2, 'count': 5},
}

order = Order(menu)
order.add_dish('dish1', 2)
order.add_dish('dish2', 1)
print(order.checkout())