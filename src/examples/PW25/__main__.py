from src.open_tasks import open_it
import os


def first_task():
    def sayHello(name):
        print("Hello!")


def second_task():
    def sayHello(name):
        print("Hello" + name)

    sayHello("Nick")


def third_task():
    def sayHello(name="Piter"):
        print("Hello" + name)

    sayHello("Nick")


def fourth_task():
    def getSum(num1, num2):
        total = num1 + num2
        return total

    s = getSum(2, 3)
    print(s)


def fifth_task():
    def sort2(a, b):
        if a < b:
            return a, b
        else:
            return b, a

    a = int(input())
    b = int(input())
    minimum, maximum = sort2(a, b)
    print(minimum, maximum)


def sixth_task():
    def mySum(*args):
        nowSum = 0
        for now in args:
            nowSum += now
        return nowSum

    print(mySum(1, 2))
    print(mySum(1, 2, 3, 4))


def seventh_task():
    def myMin(first, *others):
        nowMin = first
        for now in others:
            if now < nowMin:
                nowMin = now
            return nowMin

    print(myMin(1))
    print(myMin(3, 1, 2))


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
