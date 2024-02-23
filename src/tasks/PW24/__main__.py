from src.open_tasks import open_it
import os


def first_task():
    string = input("Введіть слово для перевірки на паліндромність: ")
    print("YES" if string == string[::-1] else "NO")


def second_task():
    string = input("Введіть речення для підрахунки слів паліндромів: ").split(" ")
    count = 0
    for word in string:
        count += 1 if word == word[::-1] else 0
    print(f"Слів паліндромів: {count}")


def third_task():
    string = input(
        "Введіть речення для підрахунки слів, які починаються на 'ф': "
    ).split(" ")
    count = 0
    for word in string:
        count += 1 if word[0] == "ф" else 0
    print(f"К-ть слів, які починаються на 'ф': {count}")


def forth_task():
    string = list(input("Введіть речення: "))
    count = {"upper": 0, "lower": 0}
    for char in string:
        count["upper"] += 1 if char.isupper() else 0
        count["lower"] += 1 if char.islower() else 0
    print(f"К-ть великих букв: {count['upper']}")
    print(f"К-ть малих букв: {count['lower']}")


def fiveth_task():
    string = input("Введіть речення: ").split(" ")
    target = ""
    for word in string:
        target = word if len(target) < len(word) else target
    print(f"Слово '{target}' найдовше")


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
