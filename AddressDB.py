import sqlite3
connection = sqlite3.connect("/home/vino/Documents/oo/Address-Book-master/data.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
#cursor.execute('''DROP TABLE Address;''')
connection.execute("create table Address (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL,phone VARCHAR(15) UNIQUE NOT NULL , address TEXT NOT NULL,city TEXT NOT NULL,state TEXT NOT NULL,country TEXT NOT NULL)")
print("Table created successfully")
connection.close()   
