from src.open_tasks import open_it
import os


def first_task():
    mySet = set (map(int, input().split()))
    print(len(mySet))


def second_task():
    set1 = set (map (int, input () .split ()))
    set2 = set (map (int, input () .split ()))
    print (*sorted (set1 & set2))

def third_task():
    text0 = input ()
    word = text0.split ()
    myset = set (word)
    print (len (myset) )


def fourth_task():
    mySet = set (map(int, input().split()))
    print(len(mySet))


def fifth_task():
    mySet = set (list (input ()) )
    print (*sorted (mySet) )


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
