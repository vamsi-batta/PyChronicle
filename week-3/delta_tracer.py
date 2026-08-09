import sqlite3
from datetime import datetime


class DeltaTracer:

    def __init__(self):
        self.previous_values = {}

        # SQLite database connect
        self.conn = sqlite3.connect("pychronicle.db")
        self.cursor = self.conn.cursor()

    def track(self, variables, line_number):
        changes = {}

        for name, value in variables.items():

            # First time variable kanipisthe
            if name not in self.previous_values:
                changes[name] = {
                    "old": None,
                    "new": value
                }

            # Value change ayithe
            elif self.previous_values[name] != value:
                changes[name] = {
                    "old": self.previous_values[name],
                    "new": value
                }

        # Current values save cheyyadam
        self.previous_values.update(variables)

        # Changes database lo save cheyyadam
        for name, change in changes.items():

            self.cursor.execute("""
                INSERT INTO variable_history
                (timestamp, line_number, variable_name, value)
                VALUES (?, ?, ?, ?)
            """, (
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                line_number,
                name,
                str(change["new"])
            ))

        self.conn.commit()

        return changes

    def close(self):
        self.conn.close()


if __name__ == "__main__":

    tracer = DeltaTracer()

    print("Step 1:")
    print(tracer.track({"x": 10, "name": "Vamsi"}, 1))

    print("Step 2:")
    print(tracer.track({"x": 10, "name": "Vamsi"}, 2))

    print("Step 3:")
    print(tracer.track({"x": 20, "name": "Vamsi"}, 3))

    print("Step 4:")
    print(tracer.track({"x": 20, "name": "Vamsi"}, 4))

    print("Step 5:")
    print(tracer.track({"x": 30, "name": "Vamsi"}, 5))

    tracer.close()