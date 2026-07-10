import sqlite3

# Connect to the database
connection = sqlite3.connect("pychronicle.db")
cursor = connection.cursor()

# Get all records from the variables table
cursor.execute("SELECT * FROM variables")

rows = cursor.fetchall()

print("Variables stored in the database:\n")

for row in rows:
    print(row)

connection.close()