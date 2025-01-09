import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race!")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Draw the finish line
finish_line = 300
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(finish_line, 250)
pen.pendown()
pen.goto(finish_line, -250)

# Create turtles
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
turtles = []
start_y = 200

for color in colors:
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(-350, start_y)
    start_y -= 80
    turtles.append(t)

# Countdown before the race
pen.penup()
pen.goto(0, 0)
pen.write("3", align="center", font=("Arial", 48, "bold"))
time.sleep(1)
pen.clear()
pen.write("2", align="center", font=("Arial", 48, "bold"))
time.sleep(1)
pen.clear()
pen.write("1", align="center", font=("Arial", 48, "bold"))
time.sleep(1)
pen.clear()
pen.write("Go!", align="center", font=("Arial", 48, "bold"))
time.sleep(1)
pen.clear()

# Start the race
is_race_on = True
while is_race_on:
    for t in turtles:
        t.forward(random.randint(5, 15))
        if t.xcor() > finish_line:
            is_race_on = False
            winner = t.pencolor()
            break

# Announce the winner
pen.goto(0, -50)
pen.write(f"The winner is {winner.upper()}!", align="center", font=("Arial", 36, "bold"))

# Keep the window open
screen.mainloop()
