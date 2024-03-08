from src.open_tasks import open_it
import os


def first_task():
    seq = map(int, input(" Введіть послідовність чисел:").split())
    countDict = {}
    for elem in seq:
        countDict[elem] = countDict.get(elem, 0) + 1
    for key in sorted(countDict):
        print(key, countDict[key], sep=" : ")


def second_task():
    s = input("Введіть речення: ")
    letters = dict()
    for c in s:
        if c not in letters:
            letters[c] = 0
        letters[c] += 1
    for c in sorted(letters):
        print(c, letters[c])


def third_task():
    keys = ["red", "green", "blue"]
    values = ["#FF0000", "#008000", "#0000FF"]
    color_dictionary = dict(zip(keys, values))
    print(color_dictionary)


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
