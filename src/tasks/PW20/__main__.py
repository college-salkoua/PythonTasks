from src.open_tasks import open_it
import os


def first_task():
    n = int(input("n: "))

    one = n
    zero = 0

    for num in range(n):
        print("0 " * zero, end="")
        print("1 " * one)
        one -= 1
        zero += 1


def second_task():
    n = int(input("n: "))
    m = int(input("m: "))
    numbers_list = []
    result = 0
    for _ in range(n):
        numbers_list.append(list(map(int, input("").split(" "))))
    for i in range(n):
        for j in range(m):
            if numbers_list[i][j] % 3 == 0:
                result += numbers_list[i][j]
    print(result)


def third_task():
    n = int(input("n: "))
    matrix = [list(map(int, input("").split())) for _ in range(n)]
    result = 0
    count_element = 0
    for i in range(n):
        for j in range(len(matrix[i])):
            if j % 2 != 0:
                result += matrix[i][j]
                count_element += 1

    print(result, (result / count_element))


def fourth_task():
    n = int(input("Введіть розмірність матриці n: "))
    matrix = [
        [int(input(f"Елемент [{i + 1},{j + 1}]: ")) for j in range(n)] for i in range(n)
    ]
    lens = len(matrix)

    print("Початкова матриця:")
    for row in matrix:
        print(row)

    for i in range(lens):
        matrix[i][0], matrix[i][lens - 1] = matrix[i][lens - 1], matrix[i][0]
    print("\nМатриця після заміни:")
    for row in matrix:
        print(row)


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
