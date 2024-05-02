import os
from src.open_tasks import open_it
import tkinter as tk


def first_task():
    def draw():
        canvas.delete('all')
        try:
            x = int(entry.get())
            y = x
            for i in range(10):
                canvas.create_rectangle(0, 0, x, y, outline='purple')
                x += x
                y += y
        except:
            pass

    root = tk.Tk()
    root.geometry('300x200')
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()

    label = tk.Label(root, text="Введіть розмір квадрату:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Намалювати", command=draw)
    button.pack()

    root.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")