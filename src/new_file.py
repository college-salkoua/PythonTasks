import os


def main():
    print("1 - create file tasks\n2 - create file examples")
    request = input("Enter 1 or 2: ")

    while request not in ["1", "2"]:
        request = input("Enter 1 or 2: ")

    if request == "1":
        path = "tasks"
        pw_name = input("Enter PW name: ")
        path = os.path.join(path, f"PW{pw_name}")

        if os.path.exists(path):
            print("This PW already exists")
            return

        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "__main__.py"), "w") as file:
            text = (
                "import os\n"
                "from src.open_tasks import open_it\n\n\n\n"
                "try:\n"
                "    open_it(str(os.path.relpath(__file__)))\n"
                "except Exception as e:\n"
                '    print(f"У вас помилка: {e}")'
            )
            file.write(text)

    elif request == "2":
        path = "examples"
        pw_name = input("Enter PW name: ")
        path = os.path.join(path, f"PW{pw_name}")

        if os.path.exists(path):
            print("This PW already exists")
            return

        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "__main__.py"), "w") as file:
            text = (
                "import os\n"
                "from src.open_tasks import open_it\n\n\n\n"
                "try:\n"
                "    open_it(str(os.path.relpath(__file__)))\n"
                "except Exception as e:\n"
                '    print(f"У вас помилка: {e}")'
            )
            file.write(text)


while True:
    print("====================================")
    print("If you wanna exit press ctrl + c")
    print("====================================\n\n")
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
