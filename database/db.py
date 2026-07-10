import sqlite3

# Connect to the database (creates it if it doesn't exist)
connection = sqlite3.connect("pychronicle.db")

cursor = connection.cursor()

# Create the variables table
cursor.execute("""
CREATE TABLE IF NOT EXISTS variables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    line_number INTEGER,
    variable_name TEXT,
    serialized_value TEXT
)
""")

connection.commit()

print("Database and table created successfully!")

connection.close()