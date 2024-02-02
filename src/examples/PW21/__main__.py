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


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}.")

