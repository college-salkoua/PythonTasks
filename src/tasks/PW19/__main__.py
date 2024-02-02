from random import randint
from src.open_tasks import open_it
import os


def first_task():
    lists = [randint(1, 5) for x in range(int(input("n: ")) + 1)]
    result = 0
    for num in lists:
        if num % 2 == 0:
            result += num
    print(lists, "\n", result)


def second_task():
    n = int(input("n: "))
    matrix = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
    result = 0
    for line in matrix:
        print(*line)
        if matrix.index(line) % 2 == 0:
            result += sum(line)
    print(result)


def third_task():
    input_list = [
        int(x) for x in input("Введіть 7 цілих чисел, розділених прогалинами: ").split()
    ]

    sorted_list = sorted(input_list)

    num1 = sorted_list[0]
    num2 = sorted_list[1]
    num3 = sorted_list[2]
    sum1 = num1 + num2
    sum2 = num1 + num3
    sum3 = num2 + num3
    sum_total = num1 + num2 + num3

    print(f"Три числа: {num1}, {num2}, {num3}")
    print(f"Можливі суми: {sum1}, {sum2}, {sum3}, {sum_total}")


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
