import os
from src.open_tasks import open_it
import tkinter as tk
from tkinter import messagebox


def first_task():
    def encrypt():
        text = entry.get()
        key = int(entry_key.get())
        result = ""
        for i in text:
            if i.isupper():
                result += chr((ord(i) + key - 65) % 26 + 65)
            elif i.islower():
                result += chr((ord(i) + key - 97) % 26 + 97)
            else:
                result += i
        messagebox.showinfo("Результат", result)

    root = tk.Tk()
    root.geometry("250x250")
    root.title("Шифр Цезаря")

    label = tk.Label(root, text="Введіть текст:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    label_key = tk.Label(root, text="Введіть ключ:")
    label_key.pack()

    entry_key = tk.Entry(root)
    entry_key.pack()

    button = tk.Button(root, text="Зашифрувати", command=encrypt)
    button.pack()

    root.mainloop()


def second_task():
    def encrypt():
        key = int(entry_key.get())
        with open("message.txt", "r") as file:
            text = file.read()
        result = ""
        for i in text:
            if i.isupper():
                result += chr((ord(i) + key - 65) % 26 + 65)
            elif i.islower():
                result += chr((ord(i) + key - 97) % 26 + 97)
            else:
                result += i
        messagebox.showinfo("Результат", result)

    root = tk.Tk()
    root.geometry("250x250")
    root.title("Шифр Цезаря")

    label_key = tk.Label(root, text="Введіть ключ:")
    label_key.pack()

    entry_key = tk.Entry(root)
    entry_key.pack()

    button = tk.Button(root, text="Зашифрувати", command=encrypt)
    button.pack()

    root.mainloop()


def third_task():
    def encrypt():
        key = int(entry_key.get())
        with open("message.txt", "r") as file:
            text = file.read()
        result = ""
        for i in text:
            if i.isupper():
                result += chr((ord(i) + key - 65) % 26 + 65)
            elif i.islower():
                result += chr((ord(i) + key - 97) % 26 + 97)
            else:
                result += i
        with open("encrypted_message.txt", "w") as file:
            file.write(result)
        messagebox.showinfo("Результат", result)

    root = tk.Tk()
    root.geometry("250x250")
    root.title("Шифр Цезаря")

    label_key = tk.Label(root, text="Введіть ключ:")
    label_key.pack()

    entry_key = tk.Entry(root)
    entry_key.pack()

    button = tk.Button(root, text="Зашифрувати", command=encrypt)
    button.pack()

    root.mainloop()


def forth_task():
    def encrypt():
        key = int(entry_key.get())
        with open("message.txt", "r") as file:
            text = file.read()
        result = ""
        for i in text:
            result += chr((ord(i) + key) % 1105)
        with open("encrypted_message.txt", "w") as file:
            file.write(result)
        messagebox.showinfo("Результат", result)

    def decrypt():
        key = int(entry_key.get())
        with open("encrypted_message.txt", "r") as file:
            text = file.read()
        result = ""
        for i in text:
            result += chr((ord(i) - key) % 1105)
        with open("decrypted_message.txt", "w") as file:
            file.write(result)
        messagebox.showinfo("Результат", result)

    root = tk.Tk()
    root.geometry("250x250")
    root.title("Шифр Цезаря")

    label_key = tk.Label(root, text="Введіть ключ:")
    label_key.pack()

    entry_key = tk.Entry(root)
    entry_key.pack()

    button = tk.Button(root, text="Зашифрувати", command=encrypt)
    button.pack()

    button_decrypt = tk.Button(root, text="Розшифрувати", command=decrypt)
    button_decrypt.pack()

    root.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
