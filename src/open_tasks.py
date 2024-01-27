import ast
import importlib


def open_it(path: str):
    functions_name = get_function_names(path)
    modules = []
    for function_name in functions_name:
        modules.append(
            getattr(
                importlib.import_module(path.replace("/", ".").removesuffix(".py")),
                function_name,
            )
        )
    print(modules)


def get_function_names(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    function_names = [
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    ]
    return function_names
