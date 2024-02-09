from random import randint
from src.open_tasks import open_it
import os


def first_task():
    s = list (input () )
    k=0
    for i in range (len (s) ) :
        if s[i] . isdigit ():
            k += 1
    print(k)


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
