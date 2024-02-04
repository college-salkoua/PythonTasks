from src.open_tasks import open_it
import os


def first_task():
    string = input("Введіть текс: ")
    print("Третій символ:", string[2])
    print("Передостанній символ:", string[-2])
    print("Перші п'ять сиволів:", string[:5])
    print("Крім останніх двох символів:", string[0:-2])
    print("Всі символи з парними індексами:", string[::2])
    print("Всі символи з непарними індексами:", string[1::2])
    print("Всі символи в зворотному порядку:", string[::-1])
    print("Всі символи рядка через один в зворотному порядку:", string[::-2])
    print("Виведе довжину цього рядка:", len(string))


def second_task():
    input_str = input("Введіть текст: ")
    first_t_index = input_str.find('t')
    last_t_index = input_str.rfind('t')

    result_str = ""
    if first_t_index != -1 and last_t_index != -1 and first_t_index < last_t_index:
        result_str = input_str[:first_t_index] + input_str[last_t_index + 1:]
        print(result_str)
    else:
        print(result_str)


def third_task():
    input_string = input("Введіть текст:")
    first_index = input_string.find('t')

    last_index = input_string.rfind('t')

    if first_index == last_index and first_index != -1:
        print(f"Буква 't' зустрічається один раз, індекс: {first_index}")
    elif first_index != -1:
        print(f"Перша поява букви 't' має індекс: {first_index}")
        print(f"Остання поява букви 't' має індекс: {last_index}")


def fourth_task():
    words = input("Введіть два слова розділені пробілом:").split(" ")
    print(words[1], words[0])


def fiveth():
    words = input("Введіть два слова розділені пробілом:").split(" ")
    print(len(words))


def sixth():
    words = list(input("Введіть рядок:"))
    for index, word in enumerate(words):
        if word == "1":
            words[index] = "one"
    print("".join(words))


def seventh():
    words = list(input("Введіть рядок:"))
    for index, word in enumerate(words):
        if word == "@":
            words.pop(word)
    print("".join(words))


def eighth():
    N, K = map(int, input().split())
    words = input().split()
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) <= K:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            print(" ".join(current_line))
            current_line = [word]
            current_length = len(word) + 1

    print(" ".join(current_line))


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
