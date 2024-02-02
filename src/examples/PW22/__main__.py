from random import randint
from src.open_tasks import open_it
import os


def first_task():
    string = input()
    substring = input()
    pos = string.find(substring)
    while pos != -1:
        print(pos)
        pos = string.find(substring, pos + 1)


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
