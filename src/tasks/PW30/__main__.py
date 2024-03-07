import os
from src.open_tasks import open_it


"""
Виконайте завдання:

1. Дано рядок тексту. Створити програму, яка порахує кількість різних слів в даному тексті. Розділові знаки
ставляться зразу після слова.
2. Дано рядок тексту. Створити програму, яка порахує кількість голосних літер в даному тексті.
3. Дано рядок тексту. Створити програму, яка порахує кількість різних слів-паліндромів є в даному тексті.
Якщо одне й те саме слово зустрічається кілька раз, то рахується тільки один раз. Розділові знаки ставляться
зразу після слова.
4. Дано рядок цифр. Створити програму, яка порахує суму різних чисел в даному рядку. Якщо число
зустрічається кілька разів, то додаємо його один раз.
5.Дано текст із маленьких латинських літер, який закінчується крапкою. Надрукувати всі літери, входять в
текст лише один раз.
6.Дано текст із маленьких латинських літер, який закінчується крапкою. Надрукувати всі літери, які входять
в текст не менше двох разів.
7.Дано текст із маленьких латинських літер, який закінчується крапкою. Надрукувати (по одному разу) в
алфавітному порядку всі голосні літери, що входять в текст.
8.Дано 100 цілих чисел від 1 до 50. Визначити, скільки серед них є чисел, перша цифра в запису яких – 1 або
2.
9. Дано рядок тексту. Створити програму, яка порахує кількість слів в даному тексті, які зустрічаються
більше двох разів. Розділові знаки ставляться зразу після слова.
"""


def first_task():
    text = input("Введіть текст: ")
    words = text.split()
    print(f"Кількість різних слів в даному тексті: {len(set(words))}")


def second_task():
    text = input("Введіть текст: ")
    vowels = "aeiou"
    vowels_count = sum(1 for letter in text if letter in vowels)
    print(f"Кількість голосних літер в даному тексті: {vowels_count}")


def third_task():
    text = input("Введіть текст: ")
    words = text.split()
    palindromes = [word for word in words if word == word[::-1]]
    print(
        f"Кількість різних слів-паліндромів є в даному тексті: {len(set(palindromes))}"
    )


def fourth_task():
    text = input("Введіть текст: ")
    numbers = [int(word) for word in text.split() if word.isdigit()]
    print(f"Сума різних чисел в даному рядку: {sum(set(numbers))}")


def fifth_task():
    text = input("Введіть текст: ")
    print(f"Літери, входять в текст лише один раз: {sorted(set(text[:-1]))}")


def sixth_task():
    text = input("Введіть текст: ")
    letters = [letter for letter in text if text.count(letter) > 1]
    print(f"Літери, які входять в текст не менше двох разів: {sorted(set(letters))}")


def seventh_task():
    text = input("Введіть текст: ")
    vowels = "aeiou"
    vowels = [letter for letter in text if letter in vowels]
    print(f"Голосні літери, що входять в текст: {sorted(set(vowels))}")


def eighth_task():
    numbers = [int(input(f"Введіть {i + 1} число: ")) for i in range(100)]
    numbers = [number for number in numbers if 1 <= number <= 50]
    print(f"Кількість чисел, перша цифра в запису яких – 1 або 2: {len(numbers)}")


def ninth_task():
    text = input("Введіть текст: ")
    words = text.split()
    words_count = {word: words.count(word) for word in words if words.count(word) > 2}
    print(
        f"Кількість слів в даному тексті, які зустрічаються більше двох разів: {len(words_count)}"
    )


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
