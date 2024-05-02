import os
from src.open_tasks import open_it
import tkinter as tk


def first_task():
    root = tk.Tk()
    root.geometry('300x200')
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    x = 0
    y = 0
    for i in range(10):
        canvas.create_oval(x, y, x + 30, y + 30, outline='purple')
        x += 30
        y += 30
    root.mainloop()


def second_task():
    root = tk.Tk()
    root.geometry('300x200')
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    x = 0
    y = 0
    for i in range(10):
        canvas.create_text(x + 15, y + 15, text="Python", fill='purple')
        x += 30
        y += 30
    root.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")