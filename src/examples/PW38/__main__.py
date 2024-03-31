from tkinter import *
from tkinter import messagebox
from src.open_tasks import open_it
import os


def first_task():
    def click():
        messagebox.showinfo(" Повідомлення", "Я ж просив не нажимати! ")
        
    window = Tk()
    window.title("Приклад вікна повідомлення")
    window.geometry('400x250')

    btn = Button(window, text="Не нажимати", bg="red",command=click)
    btn.pack()

    window.mainloop()

def second_task():
    def click():
        messagebox.showinfo(" Повідомлення", "Я ж просив не нажимати! ")
            
    window = Tk()
    window.title("Приклад вікна повідомлення")
    window.geometry('400x250')

    btn = Button(window, text="Не нажимати", bg="red",command=click)
    btn.pack()

    window.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
