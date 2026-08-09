import sqlite3


def get_state(target_line):

    conn = sqlite3.connect("pychronicle.db")
    cursor = conn.cursor()

    # Requested line varaku records fetch cheyyadam
    cursor.execute("""
        SELECT line_number, variable_name, value
        FROM variable_history
        WHERE line_number <= ?
        ORDER BY id
    """, (target_line,))

    rows = cursor.fetchall()

    state = {}

    for line_number, variable_name, value in rows:
        state[variable_name] = value

    conn.close()

    return state


def line_exists(target_line):

    conn = sqlite3.connect("pychronicle.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1
        FROM variable_history
        WHERE line_number = ?
        LIMIT 1
    """, (target_line,))

    result = cursor.fetchone()

    conn.close()

    return result is not None


target_line = int(input("Enter line number: "))

if not line_exists(target_line):

    print()
    print("No history found for line", target_line)

else:

    state = get_state(target_line)

    print()
    print("State at line", target_line, ":")

    for name, value in state.items():
        print(name, "=", value)