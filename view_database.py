import sqlite3

# Connect to the database
conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

# Fetch all records
cursor.execute("SELECT * FROM variable_history")
records = cursor.fetchall()

# Print records
print("Database Records:\n")

for record in records:
    print(record)

# Close the connection
conn.close()