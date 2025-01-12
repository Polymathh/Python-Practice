import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 0)

def display_time():
    pen.clear()
    current_time = time.strftime("%H:%M:%S")
    pen.write(current_time, align="center", font=("Arial", 48, "bold"))
    screen.ontimer(display_time, 1000)

display_time()
screen.mainloop()
