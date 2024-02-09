from models import Customer, Product, Order

class BusinessLogic:
    def __init__(self, db):
        self.db = db

    def register_customer(self, username, password):
        try:
            self.db.start_transaction()
            customer = Customer(username, password)
            customer.register(self.db)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def login_customer(self, username, password):
        try:
            return self.db.login_customer(username, password)
        except Exception as e:
            raise e

    def register_product(self, name, quantity):
        try:
            self.db.start_transaction()
            product = Product(name, quantity)
            product.register(self.db)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def place_order(self, customer_id, product_id, quantity):
        try:
            self.db.start_transaction()
            order = Order(customer_id, product_id, quantity)
            order.place_order(self.db)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def get_user_type(self, user_id):
        try:
            return self.db.get_user_type(user_id)
        except Exception as e:
            raise e

    def view_products(self):
        try:
            return self.db.view_products()
        except Exception as e:
            raise e

    def register_user(self, username, password):
        try:
            self.db.start_transaction()
            customer = Customer(username, password)
            customer.register(self.db)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def purchase_product(self, user_id, product_id, quantity):
        try:
            self.db.start_transaction()
            order = Order(user_id, product_id, quantity)
            order.place_order(self.db)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def view_orders(self, user_id):
        try:
            return self.db.view_orders(user_id)
        except Exception as e:
            raise e
