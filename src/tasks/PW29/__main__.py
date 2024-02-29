import os
from src.open_tasks import open_it


def first_task():
    sentence1 = input("Напишіть перше речення: ")
    sentence2 = input("Напишіть друге речення: ")
    letters = set(sentence1) & set(sentence2)
    print("Букви що зустрічаються в обох реченнях:", letters)


def second_task():
    sentence1 = input("Напишіть перше речення: ")
    sentence2 = input("Напишіть друге речення: ")
    letters = set(sentence1) ^ set(sentence2)
    print("Букви що зустрічаються тільки в одному з речень:", letters)


def third_task():
    sentence1 = input("Напишіть перше речення: ")
    sentence2 = input("Напишіть друге речення: ")
    vowels = "аеиіоуяюєї"
    vowels1 = set(filter(lambda x: x in vowels, sentence1))
    vowels2 = set(filter(lambda x: x in vowels, sentence2))
    vowels = vowels1 & vowels2
    print("Голосні букви які зустрічались у реченнях:", vowels)


def fourth_task():
    n = int(input("Введіть к-ть студентів"))
    languages = [set(input(f"Введіть мову для {i + 1} студента: ").split()) for i in range(n)]
    all_languages = set.intersection(*languages)
    any_languages = set.union(*languages)
    print(f"Мову що знають всі студенти: {all_languages}")
    print(f"Мову що знає хоча б один студент: {any_languages}")


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
