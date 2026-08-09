import sqlite3


def search_history(variable_name, line_number):

    conn = sqlite3.connect("pychronicle.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT value
        FROM variable_history
        WHERE variable_name = ?
        AND line_number = ?
        ORDER BY id DESC
        LIMIT 1
    """, (variable_name, line_number))

    row = cursor.fetchone()

    conn.close()

    return row


variable_name = input("Enter variable name: ")
line_number = int(input("Enter line number: "))

result = search_history(variable_name, line_number)

print()

if result:
    print("Result:")
    print(variable_name, "=", result[0])
else:
    print(
        "No history found for",
        variable_name,
        "at line",
        line_number
    )