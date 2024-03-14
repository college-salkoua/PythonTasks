import os
from src.open_tasks import open_it


def fist_task():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    try:
        result = (abs(x - 1) ** 0.5 - abs(y) ** 0.5) / (1 + (5 - x) ** 0.5)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Для даного значення аргументу функція не існує")


def second_task():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    try:
        result = (abs(x - 3) ** 0.5 - 2) / (4 - y**2)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Для даного значення аргументу функція не існує")


def third_task():
    x = float(input("Enter x: "))
    try:
        result = (1 + 6 * x) / (2 - (x - 2) ** 0.5)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Для даного значення аргументу функція не існує")


def fourth_task():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    try:
        result = (abs(x - 3) ** 0.5) / (1 + y**2)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Для даного значення аргументу функція не існує")


def fifth_task():
    x = float(input("Enter x: "))
    try:
        result = (abs(2 - x) ** 0.5) + (1 / (x - 1))
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Для даного значення аргументу функція не існує")


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
