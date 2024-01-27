import sqlite3

conn = sqlite3.connect("./online_shop.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)''')
cursor.execute('''
    CREATE TABLE  IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY, 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders ( 
    order_id INTEGER PRIMARY KEY, 
    customer_id INTEGER NOT NULL, 
    product_id INTEGER NOT NULL, 
    quantity INTEGER NOT NULL, 
    order_date DATE NOT NULL, 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
    FOREIGN KEY (product_id) REFERENCES products(product_id) )''')

while True:
    a = int(input("1 - add product, 2 - add customer, 3 - add order"))
    if a == 1:
        product_name = input("Enter the name of product")
        product_category = input("Enter the category of product")
        product_price = input("Enter the price of product")
        cursor.execute(''' 
            INSERT INTO products (name,category,price)
            VALUES (?,?,?)''', [product_name, product_category, product_price])
        conn.commit()
    if a == 2:
        first_name = input("Enter your first name")
        last_name = input("Enter your last name")
        email = input("Enter your email address")
        cursor.execute(''' 
            INSERT INTO customers (first_name,last_name,email)
            VALUES (?,?,?)''', [first_name,last_name,email])
        conn.commit()
    if a == 3:
        customer_id = input("Enter your customer id")
        product_id = input("Enter product_id")
        quantity = input("Enter quantity of product")
        order_date = input("Enter date of order")

        cursor.execute(''' 
            INSERT INTO orders (customer_id, product_id, quantity, order_date)
            VALUES (?,?,?,?)''', [customer_id, product_id, quantity, order_date])
        conn.commit()
    if a == 4:
        break