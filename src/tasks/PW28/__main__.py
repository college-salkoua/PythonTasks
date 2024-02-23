from src.open_tasks import open_it
import os, turtle, random


def first_task():
    def  kulia (x,y):
        turtle.up()
        turtle.goto(x,y)
        turtle.width(3)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(50)
        colors = ["red", "orange", "yellow", "green", "blue", "violet", "yellow"]
        turtle.fillcolor(random.choice(colors))
        turtle.end_fill()
        turtle.up()
        turtle.goto(x-50, y+50)
        turtle.down()
        turtle.goto(x-30, y-50)
        turtle.up()
        turtle.goto(x+50, y+50)
        turtle.down()
        turtle.goto(x+30, y-50)
        turtle.up()
        turtle.goto(x-30, y-50)
        turtle.down()
        colors = ["red", "orange", "yellow", "green", "blue", "violet", "yellow"]
        turtle.fillcolor(random.choice(colors))
        turtle.begin_fill()
        turtle.goto(x+30, y-50)
        turtle.goto(x+30, y-80)
        turtle.goto(x-30, y-80)
        turtle.goto(x-30, y-50)
        turtle.end_fill()

    turtle.reset()
    for i in range(6):
        x=random.randint(-200, 200)
        y=random.randint(10, 200)
        kulia(x,y)
        
    turtle.mainloop()


def second_task():
    def  rectangle (x,y):
        turtle.width(3)
        turtle.up()
        turtle.goto(x-30, y-50)
        turtle.down()
        colors = ["red", "orange", "yellow", "green", "blue", "violet", "yellow"]
        turtle.fillcolor(random.choice(colors))
        turtle.begin_fill()
        turtle.down()
        turtle.goto(x+30, y-50)
        turtle.goto(x+30, y-80)
        turtle.goto(x-30, y-80)
        turtle.goto(x-30, y-50)
        turtle.end_fill()
        turtle.up()

    turtle.reset()
    n=int(input("Введіть кількість прямокутників= "))
    for i in range(n):
        x=random.randint(-200, 200)
        y=random.randint(10, 200)
        rectangle(x,y)
        
    turtle.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
