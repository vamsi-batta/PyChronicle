import sqlite3


def get_variable_history(variable_name):

    conn = sqlite3.connect("pychronicle.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT line_number, value
        FROM variable_history
        WHERE variable_name = ?
        AND line_number > 0
        ORDER BY id
    """, (variable_name,))

    rows = cursor.fetchall()

    conn.close()

    return rows


variable_name = input("Enter variable name: ")

history = get_variable_history(variable_name)

print()

if not history:
    print("No history found for variable", variable_name)

else:
    print("History of", variable_name, ":")

    previous_value = None

    for line_number, value in history:

        if previous_value != value:

            print(
                "Line",
                line_number,
                ":",
                previous_value,
                "->",
                value
            )

        previous_value = value