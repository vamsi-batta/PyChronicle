import sys
import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()


def trace_variables(frame, event, arg):
    if event == "line":
        line_number = frame.f_lineno

        for variable_name, value in frame.f_locals.items():

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("""
                INSERT INTO variable_history
                (timestamp, line_number, variable_name, value)
                VALUES (?, ?, ?, ?)
            """, (timestamp, line_number, variable_name, str(value)))

            conn.commit()

            print(f"Saved -> {variable_name} = {value}")

    return trace_variables


def calculate():
    x = 10
    y = 20
    z = x + y
    print("Result:", z)


sys.settrace(trace_variables)

calculate()

sys.settrace(None)

conn.close()