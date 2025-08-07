class Warehouse:
    def __init__(self):
        """
        Initialize two fields.
        """
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id, name, quantity):
        """
        Add product to inventory and plus the quantity if it has existed in inventory.
        Or just add new product to dict otherwise.
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity

    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :return: if the product_id is in inventory then return the corresponding quantity,
                or False otherwise.
        """
        if product_id in self.inventory:
            return self.inventory[product_id]['quantity']
        return False

    def create_order(self, order_id, product_id, quantity):
        """
        Create an order which includes the information of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Shipped'.
        :return False: only if product_id is not in inventory or the quantity is not adequate
        """
        if product_id not in self.inventory or self.inventory[product_id]['quantity'] < quantity:
            return False
        self.inventory[product_id]['quantity'] -= quantity
        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}

    def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :return False: only if the order_id is not in self.orders
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False

    def track_order(self, order_id):
        """
        Get the status of specific order.
        :return False: only if the order_id is not in self.orders.
        """
        if order_id in self.orders:
            return self.orders[order_id]['status']
        return False