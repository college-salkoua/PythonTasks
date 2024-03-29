import ast
import pathlib
import os


def extrac_functions():
    target_pw = input("Practical work: ").upper()
    filename = f"tasks/{target_pw}/__main__.py"
    with open(filename, "r") as file:
        file_content = file.read()
        tree = ast.parse(file_content, filename=filename)

    function = []
    prefixs = ""

    for node in reversed(list(ast.walk(tree))):
        if isinstance(node, ast.FunctionDef):
            fu_name = node.name
            fu_body = ast.get_source_segment(file_content, node)
            function.append([fu_name, fu_body, ""])
        elif isinstance(node, ast.Import):
            for import_name in node.names:
                for i, (_, func_body, prefixs) in enumerate(function):
                    if import_name.name in func_body:
                        function[i][2] = prefixs + f"import {import_name.name}\n"
        elif isinstance(node, ast.ImportFrom):
            for import_name in node.names:
                for i, (_, func_body, prefixs) in enumerate(function):
                    if import_name.name in func_body:
                        function[i][2] = (
                            prefixs + f"from {node.module} import {import_name.name}\n"
                        )

    return function, target_pw, prefixs


functions, pw, prefix = extrac_functions()

pathlib.Path(f"../send_teachers_this/{pw}").mkdir(exist_ok=True, parents=True)

[
    os.remove(os.path.join(f"../send_teachers_this/{pw}", file))
    for file in os.listdir(f"../send_teachers_this/{pw}")
    if os.path.isfile(os.path.join(f"../send_teachers_this/{pw}", file))
]

for function_name, function_body, prefix in functions:
    pathlib.Path(f"../send_teachers_this/{pw}").mkdir(exist_ok=True)
    with open(f"../send_teachers_this/{pw}/{function_name}.py", "a") as file:
        file.write(prefix + "\n\n")
        file.write(function_body)
        file.write(f"\n\n\n{function_name}()\n")
