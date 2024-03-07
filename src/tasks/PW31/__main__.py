import os
from src.open_tasks import open_it


def first_task():
    rivers = {"Amazon": "South America", "Nile": "Africa", "Dnipro": "Ukraine"}
    for river, region in rivers.items():
        print(f"The {river} runs through {region}.")


def second_task():
    pets = [{"Alex": "dog"}, {"John": "cat"}, {"Anna": "parrot"}]
    for pet in pets:
        for owner, animal in pet.items():
            print(f"{owner} is the owner of a pet - a {animal}.")


def third_task():
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }
    letter = input("Введіть букву: ")
    print(f"Ваша буква у коді Морзе: {morse.get(letter.upper())}")


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
