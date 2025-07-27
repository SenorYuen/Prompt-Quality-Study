class Warehouse:
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def add_product(self, product_id, name, quantity):
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            raise ValueError("Product not found in inventory")

    def get_product_quantity(self, product_id):
        if product_id in self.inventory:
            return self.inventory[product_id]['quantity']
        else:
            return False

    def create_order(self, order_id, product_id, quantity):
        if product_id in self.inventory and self.inventory[product_id]['quantity'] >= quantity:
            self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
            self.update_product_quantity(product_id, -quantity)
            return True
        else:
            return False

    def change_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
            return True
        else:
            return False

    def track_order(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]['status']
        else:
            return False