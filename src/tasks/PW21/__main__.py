from src.open_tasks import open_it
import os
from random import randint


def first_task():
    n = int(input("n: "))
    matrix = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
    a = 0
    b = 0
    c = 0

    enum = 0
    for lists in matrix:
        a += lists[enum]
        b += sum(lists)
        if enum % 2 != 0:
            c += sum(lists)

        enum += 1
    print("Матриця:")
    for tab in matrix:
        print(*tab)
    print("сумa всіх елементів на головній діагоналі:", a)
    print("сумa елементів кожного стовпця:", b)
    print("сумa елементів парних рядків:", c)


def second_task():
    one = 10
    zero = 0

    for num in range(10):
        print("1 " * one, end="")
        print("0 " * zero)
        one -= 1
        zero += 1


def third_task():
    n = int(input("Введіть кількість рядків/стовпців n: "))

    matrix = []
    print("Введіть елементи таблиці (рядок за рядком):")
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    rows_to_swap = n // 2

    for i in range(rows_to_swap):
        matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

    print("\nРезультат обміну рядків:")
    for row in matrix:
        print(" ".join(map(str, row)))


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
