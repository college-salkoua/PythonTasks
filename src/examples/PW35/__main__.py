from tkinter import *
from src.open_tasks import open_it
import os


def first_task():
    window = Tk()
    window.title("Перше вікно")
    window.geometry("400x300")
    window.mainloop()


def second_task():
    window = Tk()
    window.title("Перше вікно")
    window.geometry("400x300")
    label1 = Label(window, text="Hello, Tkinter!")
    label1.pack()
    window.mainloop()


def third_task():
    window = Tk()
    window.title("Перше вікно")
    window.geometry("400x300")

    label1 = Label(
        text="Hello, Tkinter!",
        font=("Comic Sans", 25, "bold italic underline"),
        bg="black",
        fg="white",
        width=30,
        height=50,
    )
    label1.pack()

    window.mainloop()


def fourth_task():
    window = Tk()
    window.title("Prog")
    window.geometry("600x500")
    img = PhotoImage(file="Example.png")
    Label(image=img).pack()
    Label(text="VVPC", font=("Comic Sans", 25, "bold ")).pack()
    window.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
