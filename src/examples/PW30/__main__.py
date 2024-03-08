from src.open_tasks import open_it
import os


def first_task():
    r = input().lower()
    rm = r.split()
    k = len(set(rm))
    print(k)


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
