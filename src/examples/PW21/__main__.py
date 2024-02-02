from random import randint
from src.open_tasks import open_it
import os


def first_task():
    n = int(input())
    a = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(randint(0, 10))
        a.append(r)

    print("масив:")
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()

    m = int(input("Введіть шукане число "))

    for i in range(n):
        for j in range(n):
            if a[i][j] == m:
                print("Дане число знаходиться в ряді %d нa мicці %d" % (i, j))

    print()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}.")
