from tkinter import *
from tkinter import messagebox
import math
from src.open_tasks import open_it
import os


def first_task():
    def change():
        window.config(bg="red")

    window = Tk()
    window.title("Зміна кольору вікна")
    window.geometry("400x300")

    btn = Button(
        text="Red",
        padx="40",
        pady="60",
        font="30",
        command=change,
    )
    btn.pack()
    window.mainloop()


def second_task():
    def hello():
        label1["text"] = "Привіт!"

    window = Tk()
    window.title("Привітання")
    window.geometry("400x300")

    btn = Button(text="Натисніть!", command=hello)
    btn.pack()
    label1 = Label(text=" Чекаю !", height=50)
    label1.pack()
    window.mainloop()


def third_task():
    clicks = 0

    def click_button():
        global clicks
        clicks += 1
        label1["text"] = "Клік №{}".format(clicks)

    window = Tk()
    window.title("підрахунок кліків")
    window.geometry("400x300")

    btn = Button(
        text="Натисніть!",
        background="#f55",
        foreground="#dcc",
        padx="40",
        pady="60",
        font="30",
        command=click_button,
    )

    btn.pack()
    label1 = Label(text="Кліки")
    label1.pack()
    window.mainloop()


def fourth_task():
    clicks = 0

    def click_button():
        global clicks
        clicks += 1
        buttonText.set("Click's {}".format(clicks))

    window = Tk()
    window.title("підрахунок кліків")
    window.geometry("400x300")

    buttonText = StringVar()
    buttonText.set("Click's {}".format(clicks))

    btn = Button(
        textvariable=buttonText,
        background="#555",
        foreground="#ccc",
        padx="20",
        pady="8",
        font="16",
        command=click_button,
    )
    btn.pack()
    window.mainloop()


def fifth_task():
    def click_button():
        clicks.set(clicks.get() + 1)

    window = Tk()
    window.title("підрахунок кліків")
    window.geometry("400x300")

    clicks = IntVar()
    clicks.set(0)

    btn = Button(
        textvariable=clicks,
        background="#555",
        foreground="#ccc",
        padx="20",
        pady="8",
        font="16",
        command=click_button,
    )
    btn.pack()
    window.mainloop()


def sixth_task():
    def click():
        res = " Привіт " + txt.get()
        Ibl.configure(text=res)

    window = Tk()
    window.title("Працюємо з Entry ")
    window.geometry("400x250")
    Ibl = Label(window, text="Введіть своє імя і натисніть кнопку Привітання")
    Ibl.pack()
    txt = Entry(window, width=20)
    txt.pack()
    btn = Button(window, text="Привітання", bg="red", command=click)
    btn.pack()

    window.mainloop()


def seventh_task():
    def click():
        res = txt.get() + "! Я ж просив не нажимати! "
        messagebox.showinfo(" Повідомлення ", res)

    window = Tk()
    window.title("Працюємо з Entry ")
    window.geometry("400x250")
    Ibl = Label(window, text="Введіть своє імя ")
    Ibl.pack()
    txt = Entry(window, width=20)
    txt.pack()
    btn = Button(window, text="Не нажимати", bg="red", command=click)
    btn.pack()

    window.mainloop()


def eighth_task():
    def suma():
        lb3.config(text=int(a.get()) + int(b.get()))

    window = Tk()
    window.title("Працюємо з Entry ")
    window.geometry("400x250")
    Ib1 = Label(window, text="Введіть перше число")
    Ib1.pack()
    a = Entry(window, width=20)
    a.pack()
    Ib2 = Label(window, text="Введіть друге число")
    Ib2.pack()
    b = Entry(window, width=20)
    b.pack()
    lb3 = Label(window, text="")
    lb3.pack()

    btn = Button(window, text="CyMa", command=suma)
    btn.pack()


def nineth_task():
    def aria():
        number_a = float(a.get())
        number_b = float(b.get())
        number_c = float(c.get())
        p = (number_a + number_b + number_c) / 2
        s = math.sqrt(p * (p - number_a) * (p - number_b) * (p - number_c))
        Ib4.config(text="Площа трикутника =" + str(s))

    window = Tk()
    window.title("Працюємо з Entry ")
    window.geometry("400x250")
    Ib1 = Label(window, text="Введіть сторону а")
    Ib1.pack()
    a = Entry(window, width=20)
    a.pack()
    Ib2 = Label(window, text="Введіть сторону b")
    Ib2.pack()
    b = Entry(window, width=20)
    b.pack()
    Ib3 = Label(window, text="Введіть сторону с")
    Ib3.pack()
    c = Entry(window, width=20)
    c.pack()
    Ib4 = Label(window, text=" Площа трикутника ")
    Ib4.pack()
    btn = Button(window, text="Обчислити", command=aria)
    btn.pack()
    window.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
