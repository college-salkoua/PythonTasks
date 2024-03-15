from src.open_tasks import open_it
import os


def first_task():
    print("Приклад обробки винятків")
    try:
        n = int(input("Введіть число: "))
        rezultat = 10 / n
        print(rezultat)
    except:
        print("Не коректні дані")
    print(" Продовження програми")


def second_task():
    print("Приклад обробки винятків")
    try:
        n = int(input("Введіть число: "))
        rezultat = 10 / n
        print(rezultat)
    except (ValueError, ZeroDivisionError):
        print("Не коректні дані")
        print(" Продовження програми")


def third_task():
    print("Приклад 3 обробки винятків")
    try:
        n = int(input("Введіть ціле число: "))
        rezultat = 10 / n
        print(rezultat)
    except ValueError:
        print("введено не ціле число")
    except ZeroDivisionError:
        print("ділити на 0 не можна!")
    except:
        print("Помилка !")


def fourth_task():
    print("Приклад 4 обробки винятків")
    try:
        n = int(input("Введіть ціле число: "))
        rezultat = 10 / n
        print(rezultat)
    except ValueError:
        print("введено не ціле число")
    except ZeroDivisionError:
        print("ділити на 0 не можна!")
    except:
        print("Помилка !")
    else:
        print(" Продовження програми")


def fifth_task():
    print("Приклад 5 обробки винятків")
    while True:
        try:
            n = int(input("Введіть число: "))
            rezultat = 10 / n
            print(rezultat)
        except:
            print("Не коректні дані")


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
