import os
from src.open_tasks import open_it


def first_task():
    with open("in.dat", "r") as file:
        numbers = [int(number) for number in file.read().split()]
    print(
        f"Кількість парних чисел в даному файлі: {sum(1 for number in numbers if number % 2 == 0)}"
    )


def second_task():
    with open("chisla.dat", "r") as file:
        numbers = [float(number) for number in file.read().split()]
    print(
        f"Кількість чисел в даному файлі, які більші від 5 але менші рівні 15: {sum(1 for number in numbers if 5 < number <= 15)}"
    )


def third_task():
    with open("input.txt", "r") as file:
        text = file.read()
    print(f"Кількість літер f в даному тексті: {text.count('f')}")


def fourth_task():
    with open("input.txt", "r") as file:
        numbers = [int(number) for number in file.read().split()]
    numbers = sorted(numbers)
    print(f"A = {numbers[0]}, B = {numbers[1]}, C = {numbers[2]}")


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
