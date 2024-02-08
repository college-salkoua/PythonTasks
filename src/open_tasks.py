import ast
import importlib
import re
import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


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

    kind = path.split("/")[2]
    pattern = r"PW(\d+)"
    match = re.search(pattern, path)

    task_str = (
        "завдання" if len(modules) == 1 or len(modules) in [2, 3, 4] else "завдань"
    )
    main_name = "Практична" if kind == "tasks" else "Приклади до практичної"

    while True:
        clear_console()
        print(f"{main_name} {match.group(1)}:\nМістить {len(modules)} {task_str}")
        want_tasks = int(input("\nОберіть завдання: ")) - 1
        print()
        try:
            modules[want_tasks]()
        except Exception as e:
            print()
            print(f"Виникла помилка {e}")
        input("\nНатисніть Enter...")


def get_function_names(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    function_names = [
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    ]
    return function_names
