import os
from src.open_tasks import open_it
import tkinter as tk


def first_task():
    import random
    root = tk.Tk()
    root.geometry('250x250')
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()
    faces = [tk.PhotoImage(file=f"src/tasks/PW47/face{i}.png") for i in range(9)]
    for i in range(9):
        canvas.create_image(random.randint(0, 1000), random.randint(0, 1000), image=faces[i])
    root.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")