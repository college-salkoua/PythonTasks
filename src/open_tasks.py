import ast
import importlib


def open_it(path: str):
    functions_name = get_function_names(path)
    modules = []
    for function_name in functions_name:
        modules.append(importlib.import_module(function_name))
    print("Виберіть яке завдання запустити: ")
    ranges = range(0, len(modules))
    print(*ranges)
    want = int(input("Введіть номер завдання: "))
    if want in [*ranges]:
        function = getattr(modules[want], functions_name[want])
        function()


def get_function_names(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    function_names = [
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    ]
    return function_names
