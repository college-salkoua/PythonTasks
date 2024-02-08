import ast
import pathlib
import os


def extrac_functions():
    print(pathlib.Path(".").resolve())
    pw = input("Practical work: ").upper()
    filename = f"tasks/{pw}/__main__.py"
    with open(filename, "r") as file:
        file_content = file.read()
        tree = ast.parse(file_content, filename=filename)

    function = []

    for node in ast.walk(tree):
        print(node)
        if isinstance(node, ast.FunctionDef):
            fu_name = node.name
            fu_body = ast.get_source_segment(file_content, node)
            function.append((fu_name, fu_body))

    return function, pw


functions, pw = extrac_functions()

pathlib.Path("../send_teachers_this").mkdir(exist_ok=True)

[
    os.remove(os.path.join(f"../send_teachers_this/{pw}", file))
    for file in os.listdir(f"../send_teachers_this/{pw}")
    if os.path.isfile(os.path.join(f"../send_teachers_this/{pw}", file))
]

for function_name, function_body in functions:
    pathlib.Path(f"../send_teachers_this/{pw}").mkdir(exist_ok=True)
    with open(f"../send_teachers_this/{pw}/{function_name}.py", "a") as file:
        file.write(function_body)
        file.write(f"\n\n{function_name}()\n")
