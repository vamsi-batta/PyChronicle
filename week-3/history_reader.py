import sqlite3


def get_state(target_line):

    conn = sqlite3.connect("pychronicle.db")
    cursor = conn.cursor()

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


target_line = int(input("Enter line number: "))

state = get_state(target_line)

print()
print("State at line", target_line, ":")

for name, value in state.items():
    print(name, "=", value)