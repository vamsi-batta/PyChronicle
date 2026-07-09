import ast

code = """
x = 10
y = 20
print(x + y)
"""

tree = ast.parse(code)

print(ast.dump(tree, indent=4))