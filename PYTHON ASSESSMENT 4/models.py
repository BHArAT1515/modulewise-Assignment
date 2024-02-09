class Customer:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def register(self, db):
        query = "INSERT INTO customers (username, password) VALUES (%s, %s)"
        params = (self.__username, self.__password)
        db.execute_query(query, params)
        db.commit()

    def login(self, db):
        query = "SELECT id FROM customers WHERE username = %s AND password = %s"
        params = (self.__username, self.__password)
        result = db.execute_query(query, params)
        customer_id = result.fetchone()
        if customer_id:
            return customer_id[0]  # Return customer's ID if login successful
        else:
            return None  # Return None if login failed

    # You can add other operations related to customers here, such as updating information, deleting account, etc.


class Product:
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def register(self, db):
        query = "INSERT INTO products (name, quantity) VALUES (%s, %s)"
        params = (self.__name, self.__quantity)
        db.execute_query(query, params)
        db.commit()

    # Add other operations related to products, such as updating quantity, deleting product, etc.


class Order:
    def __init__(self, customer_id, product_id, quantity):
        self.__customer_id = customer_id
        self.__product_id = product_id
        self.__quantity = quantity

    def place_order(self, db):
        query = "INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)"
        params = self.__customer_id, self.__
