from tkinter import *
from src.open_tasks import open_it
import os


def first_task():
    def display_color_info(color_name):
        color_dict = {
            "Red": "Червоний",
            "Orange": "Помаранчевий",
            "Yellow": "Жовтий",
            "Green": "Зелений",
            "Blue": "Синій",
            "Indigo": "Темно - синій",
            "Violet": "Фіолетовий"
        }
        top_label.config(text=color_dict[color_name])
        bottom_label.config(text=color_name)
    root=Tk()
    root.title("Кольорові кнопки")
    colors=["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
    buttons=[]
    frame=Frame(root)
    frame.pack(pady=10)
    for color in colors:
        button = Button(frame, bg=color, command=lambda c=color: display_color_info(c), padx='50', pady='30')
        button.pack(side=LEFT, padx=5)
        buttons.append(button)
    top_label = Label(root, text="", font=("Times New Roman", 14))
    top_label.pack()
    bottom_label = Label(root, text="", font=("Times New Roman", 14))
    bottom_label.pack()

    root.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
