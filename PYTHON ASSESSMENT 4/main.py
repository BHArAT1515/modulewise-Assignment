import tkinter as tk
from tkinter import messagebox
from Database_Connection import DatabaseConnection
from business_logic import BusinessLogic

# Initialize database connection
db = DatabaseConnection(host="localhost", username="yourusername", password="yourpassword", database="product_management")
db.connect()

# Initialize business logic
logic = BusinessLogic(db)

def register_form():
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    tk.Label(register_window, text="Username:").grid(row=0, column=0)
    tk.Label(register_window, text="Password:").grid(row=1, column=0)
    username_entry = tk.Entry(register_window)
    password_entry = tk.Entry(register_window, show="*")
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def register():
        username = username_entry.get()
        password = password_entry.get()
        try:
            logic.register_user(username, password)
            messagebox.showinfo("Success", "Registration successful")
            register_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(register_window, text="Register", command=register).grid(row=2, column=1)

def login_form():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    tk.Label(login_window, text="Username:").grid(row=0, column=0)
    tk.Label(login_window, text="Password:").grid(row=1, column=0)
    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show="*")
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        try:
            user_id = logic.login_user(username, password)
            if user_id:
                user_type = logic.get_user_type(user_id)
                if user_type == "Product Manager":
                    product_manager(user_id)
                else:
                    customer(user_id)
                login_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(login_window, text="Login", command=login).grid(row=2, columnspan=2)

def product_manager(user_id):
    product_manager_window = tk.Toplevel(root)
    product_manager_window.title("Product Manager")
    tk.Button(product_manager_window, text="Register Product", command=register_product_form).pack()
    tk.Button(product_manager_window, text="View Products", command=view_products).pack()

def register_product_form():
    register_product_window = tk.Toplevel(root)
    register_product_window.title("Register Product")
    tk.Label(register_product_window, text="Name:").grid(row=0, column=0)
    tk.Label(register_product_window, text="Quantity:").grid(row=1, column=0)
    name_entry = tk.Entry(register_product_window)
    quantity_entry = tk.Entry(register_product_window)
    name_entry.grid(row=0, column=1)
    quantity_entry.grid(row=1, column=1)

    def register():
        name = name_entry.get()
        quantity = quantity_entry.get()
        try:
            logic.register_product(name, quantity)
            messagebox.showinfo("Success", "Product registration successful")
            register_product_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(register_product_window, text="Register", command=register).grid(row=2, columnspan=2)

def view_products():
    try:
        products = logic.view_products()
        product_list = "\n".join(str(product) for product in products)
        messagebox.showinfo("Products", product_list)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def customer(user_id):
    customer_window = tk.Toplevel(root)
    customer_window.title("Customer")
    tk.Button(customer_window, text="Purchase Product", command=purchase_product_form).pack()
    tk.Button(customer_window, text="View Orders", command=lambda: view_orders(user_id)).pack()

def purchase_product_form():
    purchase_product_window = tk.Toplevel(root)
    purchase_product_window.title("Purchase Product")
    tk.Label(purchase_product_window, text="Product ID:").grid(row=0, column=0)
    tk.Label(purchase_product_window, text="Quantity:").grid(row=1, column=0)
    product_id_entry = tk.Entry(purchase_product_window)
    quantity_entry = tk.Entry(purchase_product_window)
    product_id_entry.grid(row=0, column=1)
    quantity_entry.grid(row=1, column=1)

    def purchase():
        product_id = product_id_entry.get()
        quantity = quantity_entry.get()
        try:
            logic.purchase_product(user_id, product_id, quantity)
            messagebox.showinfo("Success", "Purchase successful")
            purchase_product_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(purchase_product_window, text="Purchase", command=purchase).grid(row=2, columnspan=2)

def view_orders(user_id):
    try:
        orders = logic.view_orders(user_id)
        order_list = "\n".join(str(order) for order in orders)
        messagebox.showinfo("Orders", order_list)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Product Management Application")

tk.Button(root, text="Register", command=register_form).pack()
tk.Button(root, text="Login", command=login_form).pack()

root.mainloop()
