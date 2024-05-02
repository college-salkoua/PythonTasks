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
    dx = 1
    dy = 1
    ball = canvas.create_oval(x, y, x + 30, y + 30, outline='purple')
    root.mainloop()
    while True:
        x += dx
        y += dy
        canvas.coords(ball, x, y, x + 30, y + 30)
        if x >= 270 or x <= 0:
            dx = -dx
        if y >= 170 or y <= 0:
            dy = -dy
        root.update()
        root.after(10)


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")