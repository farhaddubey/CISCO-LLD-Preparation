class Product(IProduct):

    def __int__(self, id, name, price, shipping_cost):
        self.id = id 
        self.name = name
        self.price = price
        self.shipping_cost = shipping_cost

    def get_id(self):
        return self.id 

    def set_id(self, ic):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_shipping_cost(self):
        return self.shipping_cost

    def set_shipping_cost(self, shipping_cost):
        self.shipping_cost = shipping_cost

class User(IUser):

    def __int__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.balance = balance 
        self.orders = [] 

    def get_id(self):
        return self.id 

    def set_id(self, id):
        self.id = id 

    def get_name(self):
        return self.name 

    def set_name(self, name):
        self.name = name 

    def get_balance(self):
        return self.balance 

    def set_balance(self, balance):
        self.balance = balance 

    def get_orders(self):
        return self.orders 

    def set_orders(self, orders):
        self.orders = orders 

class Order(IOrder):

    def __int__(self, product, quantity):
        self.product = product 
        self.quantity = quantity 

    def get_product(self):
        return self.product 

    def set_product(self, product):
        self.product = product 

    def get_quantity(self):
        return self.quantity 

    def set_quantity(self, quantity):
        self.quantity = quantity 

class Company(ICompany):

    def __init__(self):
        self.users = []
        self.products = []

    def place_order(self, user_id, product_id, quantity):

        user = None 
        product = None 

        for u in self.users:
            if u.get_id() == user_id:
                user = u 
                break

        for p in self.products:
            if p.get_id() == product_id:
                product = p 
                break 

        if user is None or product is None:
            return False 

        if quantity <= 0:
            return False 

        total_cost = (
            product.get_price()  * quantity + product.get_shipping_cost()
        )

        if user.get_balance() < l_cost : 
            return false 

        user.set_balance(
            user.get_balance() - total_cost
        )

        order = Order(product, quantity)
        user.get_orders().append(order)

        return True 
    