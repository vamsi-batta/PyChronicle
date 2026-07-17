import ast

with open("sample.py", "r") as file:
    code = file.read()

tree = ast.parse(code)

for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                print("Variable:", target.id)
                print("Line:", node.lineno)
                print("----------------")