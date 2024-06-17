import sqlite3

conn = sqlite3.connect('stock.db')


cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
               id INTEGER PRIMARY KEY,
               username  TEXT NOT NULL,
               email TEXT NOT NULL,
               password TEXT NOT NULL ,
               role TEXT
               )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
               id INTEGER PRIMARY KEY,
               product_name TEXT,
               price REAL,
               quantity INTEGER
               )
''')

cursor.execute('''
               
    CREATE TABLE IF NOT EXISTS order_item (
               id INTEGER PRIMARY KEY,
               product_id INTEGER,
               quantity INTEGER,
               FOREIGN KEY(product_id) REFERENCES product(id)
               );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
               id INTEGER PRIMARY KEY,
               product_list INTEGER,
               cashier_id INTEGER,
               FOREIGN KEY(product_list) REFERENCES order_item(id),
               FOREIGN KEY(cashier_id) REFERENCES user(id)
            );''')

conn.commit()
conn.close()