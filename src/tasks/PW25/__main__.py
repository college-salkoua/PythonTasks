"""
Завдання 2.
Розробити функцію length(x1,y1,x2,y2),яка приймає 4 аргументи – дійсні
числа(координати x , y двох точок ), та повертає дійсне число – відстань між даними
точками.
Примітка:
Відстань між двома точками визначається по формулі:

2
12
2

12)()(yyxxl
Приклад послідовності дій для тестування:
print ( length(1,1,2,2) ) # 1,414213s
"""

from src.open_tasks import open_it
import os
import math


def first_task():
    def isEven(n) -> bool:
        return True if n % 2 == 0 else False

    print(isEven(int(input("Введіть число дя перевірки: "))))


def second_task():
    def length(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(length(1, 1, 2, 2))  # 1.4142135623730951


def third_task():
    def bouquets(narcissus_price, tulip_price, rose_price, summ):
        count = 0
        for narcissus_count in range(summ // narcissus_price + 1):
            for tulip_count in range(summ // tulip_price + 1):
                for rose_count in range(summ // rose_price + 1):
                    total_price = (
                        narcissus_count * narcissus_price
                        + tulip_count * tulip_price
                        + rose_count * rose_price
                    )
                    total_flowers = narcissus_count + tulip_count + rose_count
                    if total_price <= summ and total_flowers % 2 != 0:
                        count += 1
        return count

    # Тести з прикладами
    print(bouquets(1, 1, 1, 5))  # 34
    print(bouquets(2, 3, 4, 10))  # 12
    print(bouquets(2, 3, 4, 100))  # 4019
    print(bouquets(200, 300, 400, 10000))  # 4019
    print(bouquets(200, 300, 400, 100000))  # 3524556


def forth_task():
    def find_fraction(summ):
        if summ % 2 == 0:
            return False

        numerator = (summ - 1) // 2
        denominator = numerator + 1
        return (numerator, denominator)

    # Тести з прикладами
    print(find_fraction(2))  # False
    print(find_fraction(3))  # (1, 2)
    print(find_fraction(10))  # (3, 7)
    print(find_fraction(62))  # (29, 33)
    print(find_fraction(150000001))  # (75000000, 75000001)


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
