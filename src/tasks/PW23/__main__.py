from src.open_tasks import open_it
import os


def first_task():
    text = input("Введіть текст: ").lower()
    step = 1
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    print(
        text.translate(
            str.maketrans(alpha_lower[step:] + alpha_lower[:step], alpha_lower)
        )
    )


def second_task():
    text = input("Введіть текст: ").lower()
    step = int(input("Введіть число: "))
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    print(
        "Закодованно в: ",
        encode := text.translate(
            str.maketrans(alpha_lower, alpha_lower[step:] + alpha_lower[:step])
        ),
    )
    print(
        "Розкодованно в:",
        encode.translate(
            str.maketrans(alpha_lower[step:] + alpha_lower[:step], alpha_lower)
        ),
    )


def third_task():
    text = input("Введіть текст: ").lower()
    step = int(input("Введіть ключ шифрування (від'ємне - ключ дешифрування): "))
    alpha_lower = "abcdefghijklmnopqrstuvwxyzабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    print(
        "Закодованно в: ",
        encode := text.translate(
            str.maketrans(alpha_lower, alpha_lower[step:] + alpha_lower[:step])
        ),
    )
    print(
        "Розкодованно в:",
        encode.translate(
            str.maketrans(alpha_lower[step:] + alpha_lower[:step], alpha_lower)
        ),
    )


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
