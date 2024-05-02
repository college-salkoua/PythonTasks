import os
from src.open_tasks import open_it
import tkinter as tk


def first_task():
    root = tk.Tk()
    root.geometry('250x250')
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()
    canvas.create_rectangle(50, 110, 70, 160, outline='purple')
    root.mainloop()


def second_task():
    root = tk.Tk()
    root.geometry('250x250')
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()
    canvas.create_rectangle(50, 50, 100, 100, outline='purple')
    canvas.create_rectangle(50, 50, 100, 100, outline='purple')
    canvas.create_line(50, 50, 100, 50, fill='purple')
    canvas.create_line(50, 50, 50, 100, fill='purple')
    canvas.create_line(100, 50, 100, 100, fill='purple')
    canvas.create_line(50, 100, 100, 100, fill='purple')
    root.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")