from src.open_tasks import open_it
import os


def first_task():
    fin = open("proba.txt", "r")
    for line in fin:
        print(line)
    fin.close()


def second_task():
    fin = open("proba.txt", "r")
    s = sum(map(int, fin.read().split()))
    print(s)
    fin.close()


def third_task():
    fin = open("proba.txt", "r")
    s = sum(map(int, fin.readline().split()))
    print(s)
    s = sum(map(int, fin.readline().split()))
    print(s)
    fin.close()


def fourth_task():
    fin = open("proba.txt", "r")
    for line in fin:
        print(line)
    fin.close()


def fifth_task():
    fin = open("proba.txt", "r")
    a = fin.readline().split()[0]
    b = fin.readline().split()[0]
    print(a + b)
    fin.close()


def sixth_task():
    fin = open("in.txt", "r")
    k = len(fin.read().split())
    print(k)
    fin.close()


def seventh_task():
    f = open("out.txt", "w")
    f.write("Hello \n")
    f.write("world! \n")
    f.close()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
