import turtle
import time

def draw_heart(size):
    """Draws a love heart shape of a given size."""
    turtle.penup()
    turtle.goto(0, -size * 0.4)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(size)
    turtle.circle(size * 0.4, 200)
    turtle.right(140)
    turtle.circle(size * 0.4, 200)
    turtle.forward(size)
    turtle.end_fill()

def animated_heart():
    """Draws a heart that keeps enlarging."""
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")  # Set the background color to black
    screen.title("Animated Love Heart")

    turtle.speed(0)
    turtle.color("red")
    turtle.pensize(2)

    size = 50  # Initial size of the heart

    while size < 300:  # Stop enlarging after a certain size
        turtle.clear()
        draw_heart(size)
        size += 10  # Increment the size
        turtle.setheading(0)  # Reset orientation
        time.sleep(0.3)  # Pause briefly for animation

    turtle.hideturtle()
    screen.mainloop()

animated_heart()

