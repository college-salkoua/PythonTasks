from tkinter import *
from src.open_tasks import open_it
import os


def first_task():
    window=Tk()
    window.title('Параметри прямокутника')
    window.geometry('300x100')
    lab1=Label(text='Введіть ширину')
    Label.grid(row=0, column=0)
    lab2=Label(text='Введіть висоту')
    lab2.grid(row=1, column=0)

    e1=Entry()
    e1.grid(row=0, column=1)
    e2=Entry()
    e2.grid(row=1, column=1)

    window.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
