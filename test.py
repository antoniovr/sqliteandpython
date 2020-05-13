import sqlite3
from sqlite3 import Error

# conn = sqllite3.connect(':memory:') <- would save the dataabase on memory
conn = sqlite3.connect('customer.db')

c = conn.cursor()


# Create a table using multiple lines for readability
try:
    c.execute("""
        CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
        )""")
except Error as e:
    print("fallo: ", e)

# Datatypes
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Insert a single line
# c.execute("INSERT INTO customers VALUES ('Tim', 'Smith', 'tim@gmail.com')")

# Insert many

# many_customers = [
#                     ('Wes', 'Brown', 'wes@brown.com'),
#                     ('Steph','Kuewa','steph@kuewa.com'),
#                     ('Dan','Pas','dan@pas.com')
# 
#                  ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# c.execute("SELECT * FROM customers WHERE first_name='Antonio'")

# Query
# c.execute("SELECT * FROM customers")
c.execute("SELECT DISTINCT first_name,last_name,email FROM customers ORDER BY first_name")

# text = c.fetchone()
# print(text , "\n")
# text = c.fetchmany(3)
# print(text , "\n")
text = c.fetchall()
print(text , "\n")

# commit our command
conn.commit()

# close our connection
conn.close()


