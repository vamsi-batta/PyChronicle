import sqlite3


def get_line_history(line_number):

    conn = sqlite3.connect("pychronicle.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT variable_name, value
        FROM variable_history
        WHERE line_number = ?
        ORDER BY id
    """, (line_number,))

    rows = cursor.fetchall()

    conn.close()

    return rows


line_number = int(input("Enter line number: "))

history = get_line_history(line_number)

print()

if not history:
    print("No history found for line", line_number)

else:
    print("History at line", line_number, ":")

    for variable_name, value in history:
        print(variable_name, "=", value)