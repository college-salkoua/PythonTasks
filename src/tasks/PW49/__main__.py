import os
from src.open_tasks import open_it


def second_task():
    import tkinter as tk
    import random

    def move_ball():
        global x, y, dx, dy
        canvas.move(ball, dx, dy)
        x += dx
        y += dy
        if x >= 300 or x <= 0:
            dx = -dx
        if y >= 200 or y <= 0:
            dy = -dy
        root.after(50, move_ball)

    root = tk.Tk()
    root.geometry('300x200')
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    x = random.randint(0, 300)
    y = random.randint(0, 200)
    ball = canvas.create_oval(x, y, x + 30, y + 30, fill='purple')
    dx = 5
    dy = 5
    move_ball()
    root.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")