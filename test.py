import sqlite3

# conn = sqllite3.connect(':memory:') <- would save the dataabase on memory
conn = sqlite3.connect('customer.db')

c = conn.cursor()

# Create a table using multiple lines for readability
c.execute("""
    CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
        )""")

# Datatypes
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# commit our command
conn.commit()


