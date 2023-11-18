# import the libraries to be used
import sqlite3 

#  connect to the database(or create it if it doesn't exists)
conn=sqlite3.connect("prodcuct_database.db")
cur = conn.cursor()

# establish a connection by creating a cursor object to execute SQL Commands
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
    )
''')

