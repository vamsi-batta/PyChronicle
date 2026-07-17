import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("pychronicle.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS variable_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    line_number INTEGER,
    variable_name TEXT,
    value TEXT
)
""")

print("Database and table created successfully!")

conn.commit()
conn.close()