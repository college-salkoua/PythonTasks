from src.open_tasks import open_it
import os


def first_task():
    def sum(n):
        if n == 1:
            return 1
        else:
            return n + sum(n - 1)

    n = int(input())
    print(sum(n))


def second_task():
    def Fib(n):
        if n <= 1:
            return n
        else:
            return Fib(n - 1) + Fib(n - 2)

    n = int(input())
    print(Fib(n))


def third_task():
    def move(n, start, finish):
        if n == 1:
            print("Перенести диск 1 з стержня", start, "на стержень", finish)
        else:
            temp = 6 - start - finish
            move(n - 1, start, temp)
            print("Перенести диск", n, "з стержня", start, "на стержень", finish)
            move(n - 1, temp, finish)

    move(4, 1, 3)


def fourth_task():
    def hid(x, y):
        global k

        a[x][y] = "z"
        if x - 1 < 0:
            k += 1
        else:
            if a[x - 1][y] == "#":
                k += 1
            elif a[x - 1][y] == ".":
                hid(x - 1, y)
        if x + 1 > n - 1:
            k += 1
        else:
            if a[x + 1][y] == "#":
                k += 1
            elif a[x + 1][y] == ".":
                hid(x + 1, y)

        if y - 1 < 0:
            k += 1
        else:
            if a[x][y - 1] == "#":
                k += 1
            elif a[x][y - 1] == ".":
                hid(x, y - 1)

        if y + 1 > n - 1:
            k += 1
        else:
            if a[x][y + 1] == "#":
                k += 1
            elif a[x][y + 1] == ".":
                hid(x, y + 1)

    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
    """
    for i in range(n):
        for j in range(n):
            print (a[i][j],end = '')
        print()
    """
    k = 0
    x = 0
    y = 0
    hid(x, y)
    k = k - 4
    print(k * 9)


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
