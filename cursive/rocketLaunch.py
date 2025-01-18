import turtle
import math
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Pulsing Heart Animation")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Heart drawing function
def draw_heart(t, size, color):
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.left(50)
    for _ in range(200):
        t.forward(size * math.pi / 200)  # Smooth curve
        t.left(1)
    t.left(120)
    for _ in range(200):
        t.forward(size * math.pi / 200)
        t.left(1)
    t.left(140)
    t.forward(size * 1.2)
    t.end_fill()

# Create the turtle
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)

# Animation variables
pulse_size = 50
color_palette = ["red", "pink", "magenta", "hot pink", "purple", "violet"]

# Animation loop
while True:
    heart.clear()
    random_color = random.choice(color_palette)
    draw_heart(heart, pulse_size, random_color)
    pulse_size += 5  # Pulse increase
    if pulse_size > 80:  # Reset pulse size
        pulse_size = 50
    time.sleep(0.1)
    screen.update()

# Keeps the window open (manual close)
turtle.done()
