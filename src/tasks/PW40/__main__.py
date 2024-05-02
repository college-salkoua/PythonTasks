import os
from src.open_tasks import open_it
from tkinter import messagebox, Tk, Label, Button
import random


def first_task():
    def change(event):
        x1 = random.randint(10, 200)
        y1 = random.randint(2, 240)
        event.place(x=x1, y=y1)

    def click():
        messagebox.showinfo("Результат", "Ми дуже раді за вас!")

    window = Tk()
    window.title("Опитування студентів ВПФК")
    window.geometry("400x300")
    label1 = Label(window, text="Ви задоволені навчанням в ВПФК?")
    label1.pack()

    x1 = 75
    y1 = 100
    b = Button(text='ні', width=10, height=3)
    b.bind("<Motion>", change(b))
    b.place(x=x1, y=y1)

    b2 = Button(text='так', width=10, height=3, command=click)
    b2.place(x=275, y=100)
    window.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
