from tkinter import *
from math import *
from src.open_tasks import open_it
import os


def first_task():
    def red():
        window.config(bg='red')

    def blue():
        window.config(bg='blue')

    def green():
        window.config(bg='green')
        
    window = Tk()
    window.title("Зміна кольору")
    window.geometry("300x200")
    red_button = Button(window, text="Червоний", command=red, width=10)
    red_button.pack(pady=5)
    blue_button=Button(window, text="Синій", command=blue, width=10)
    blue_button.pack(pady=5)
    green_button=Button(window, text="Зелений", command=green, width=10)
    green_button.pack(pady=5)

    window.mainloop()


def second_task():
    def calculate():
        try:
            num1=float(entry1.get())
            num2=float(entry2.get())
            sum_result=num1+num2
            difference_result=num1-num2
            product_result=num1*num2
            if num2!=0:
                quotient_result = num1 / num2
            else:
                quotient_result="Ділення на нуль!"
            sum_label.config(text=f"Сума: {sum_result}")
            difference_label.config(text=f"Різниця: {difference_result}")
            product_label.config(text=f"Добуток: {product_result}")
            quotient_label.config(text=f"Частка: {quotient_result}")
        except ValueError:
            sum_label.config(text="Помилка: введіть числа!")

    window=Tk()
    window.title("Калькулятор")
    window.geometry("300x200")
    label1=Label(window,text="Введіть перше число:")
    label1.pack()
    entry1=Entry(window)
    entry1.pack()
    label2=Label(window,text="Введіть друге число:")
    label2.pack()
    entry2=Entry(window)
    entry2.pack()
    calculate_button=Button(window, text="Обчислити", command=calculate)
    calculate_button.pack()
    sum_label=Label(window, text="")
    sum_label.pack()
    difference_label=Label(window, text="")
    difference_label.pack()
    product_label=Label(window, text="")
    product_label.pack()
    quotient_label=Label(window, text="")
    quotient_label.pack()
    window.mainloop()

def third_task():
    def calculate_distance():
        try:
            x1=float(entry_x1.get())
            y1=float(entry_y1.get())
            x2=float(entry_x2.get())
            y2=float(entry_y2.get())
            distance=sqrt((x2 - x1)**2 + (y2 - y1)**2)
            distance_label.config(text=f"Відстань між точками: {distance}")
        except ValueError:
            distance_label.config(text="Помилка: введіть числа!")

    window=Tk()
    window.title("Обчислення відстані між точками")
    window.geometry("400x400")

    label_point1=Label(window, text="Точка 1:")
    label_point1.grid(row=0, column=0)
    label_x1=Label(window, text="x:")
    label_x1.grid(row=0, column=1)
    entry_x1=Entry(window)
    entry_x1.grid(row=0, column=2)
    label_y1=Label(window, text="y:")
    label_y1.grid(row=0, column=3)
    entry_y1=Entry(window)
    entry_y1.grid(row=0, column=4)
    label_point2=Label(window, text="Точка 2:")
    label_point2.grid(row=1, column=0)
    label_x2=Label(window, text="x:")
    label_x2.grid(row=1, column=1)
    entry_x2=Entry(window)
    entry_x2.grid(row=1, column=2)
    label_y2=Label(window, text="y:")
    label_y2.grid(row=1, column=3)
    entry_y2=Entry(window)
    entry_y2.grid(row=1,column=4)
    calculate_button=Button(window, text="Обчислити відстань", command=calculate_distance)
    calculate_button.grid(row=2, columnspan=5)
    distance_label=Label(window, text="")
    distance_label.grid(row=3, columnspan=5)

    window.mainloop()


def fourth_task():
    colors=["red", "yellow", "green", "yellow"]
    color_index=0

    def change_color():
        global color_index
        window.config(bg=colors[color_index])
        color_index=(color_index + 1) % len(colors)
        color_button.config(text=colors[color_index].capitalize())
        
    window=Tk()
    window.title("Зміна кольору")
    window.geometry("300x300")
    window.config(bg="red")
    color_button=Button(window, text="Yellow", command=change_color, font=("Comics Sans", 50))
    color_button.pack(pady=70)

    window.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
