import ast
import sqlite3
from datetime import datetime

# Connect to SQLite database
connection = sqlite3.connect("pychronicle.db")
cursor = connection.cursor()

# Read the Python file
with open("sample_code/example.py", "r") as file:
    code = file.read()

# Convert Python code into AST
tree = ast.parse(code)

print("Variable Assignments:\n")

# Find all variable assignments
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):

                # Variable name
                variable_name = target.id

                # Line number
                line_number = node.lineno

                # Variable value
                if isinstance(node.value, ast.Constant):
                    value = str(node.value.value)
                else:
                    value = "Unsupported"

                # Current timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Save data into SQLite database
                cursor.execute("""
                INSERT INTO variables
                (timestamp, line_number, variable_name, serialized_value)
                VALUES (?, ?, ?, ?)
                """, (timestamp, line_number, variable_name, value))

                # Print output
                print(f"Variable: {variable_name}")
                print(f"Line Number: {line_number}")
                print(f"Value: {value}")
                print("-------------------")

# Save all changes
connection.commit()

# Close the database
connection.close()

print("All variables saved successfully!")