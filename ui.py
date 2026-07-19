from textual.app import App
from textual.widgets import Header, Footer, Static


class PyChronicleUI(App):

    def compose(self):
        yield Header()

        yield Static("""
Welcome to PyChronicle

This is Week 2 Basic UI

Features:
✔ Execution Tracing
✔ SQLite Database
✔ Variable History
        """)

        yield Footer()


if __name__ == "__main__":
    app = PyChronicleUI()
    app.run()