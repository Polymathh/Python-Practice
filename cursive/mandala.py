import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Mandala Art")
screen.bgcolor("black")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Colors for the mandala
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "white"]

def draw_mandala():
    for i in range(36):  # 36 rotations for symmetry
        # Change color randomly
        pen.color(random.choice(colors))
        # Draw a circle
        pen.circle(100)
        # Draw an inner pattern
        for _ in range(6):  # Inner repeating pattern
            pen.forward(100)
            pen.left(60)
        # Rotate the turtle for the next layer
        pen.right(10)

# Draw the mandala
draw_mandala()

# Hide the turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()


