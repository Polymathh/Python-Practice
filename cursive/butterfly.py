import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.title("Animated Butterflies in a Garden")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Function to draw a butterfly
def draw_butterfly(x, y, wing_color):
    # Butterfly's body
    body = turtle.Turtle()
    body.penup()
    body.goto(x, y)
    body.shape("circle")
    body.color("black")
    body.shapesize(0.5)
    body.speed(0)

    # Butterfly's wings
    wing1 = turtle.Turtle()
    wing1.penup()
    wing1.goto(x - 10, y + 10)
    wing1.shape("circle")
    wing1.color(wing_color)
    wing1.shapesize(2)
    wing1.speed(0)

    wing2 = turtle.Turtle()
    wing2.penup()
    wing2.goto(x + 10, y + 10)
    wing2.shape("circle")
    wing2.color(wing_color)
    wing2.shapesize(2)
    wing2.speed(0)

    wing3 = turtle.Turtle()
    wing3.penup()
    wing3.goto(x - 10, y - 10)
    wing3.shape("circle")
    wing3.color(wing_color)
    wing3.shapesize(2)
    wing3.speed(0)

    wing4 = turtle.Turtle()
    wing4.penup()
    wing4.goto(x + 10, y - 10)
    wing4.shape("circle")
    wing4.color(wing_color)
    wing4.shapesize(2)
    wing4.speed(0)

    return body, wing1, wing2, wing3, wing4

# Animate the wings
def flap_wings(wings):
    for _ in range(10):
        for wing in wings:
            wing.shapesize(random.uniform(1.5, 2.5))
        screen.update()
        time.sleep(0.1)

# Move butterflies randomly
def move_butterfly(body, wings):
    for _ in range(100):
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        body.goto(body.xcor() + dx, body.ycor() + dy)
        for wing in wings:
            wing.goto(body.xcor() + random.randint(-15, 15), body.ycor() + random.randint(-15, 15))
        flap_wings(wings)

# Draw a garden
def draw_garden():
    garden = turtle.Turtle()
    garden.speed(0)
    garden.penup()
    garden.goto(-400, -300)
    garden.color("green")
    garden.begin_fill()
    for _ in range(2):
        garden.forward(800)
        garden.left(90)
        garden.forward(300)
        garden.left(90)
    garden.end_fill()

# Draw flowers
def draw_flower(x, y):
    flower = turtle.Turtle()
    flower.penup()
    flower.goto(x, y)
    flower.speed(0)
    flower.color(random.choice(["red", "yellow", "purple", "orange"]))
    flower.shape("circle")
    flower.shapesize(1.5)

# Main program
draw_garden()

# Draw flowers
for _ in range(20):
    draw_flower(random.randint(-350, 350), random.randint(-280, -50))

# Create butterflies
butterflies = []
colors = ["red", "blue", "yellow", "purple", "pink", "orange"]
for _ in range(5):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    wing_color = random.choice(colors)
    butterflies.append(draw_butterfly(x, y, wing_color))

# Animate butterflies
while True:
    for butterfly in butterflies:
        body, wing1, wing2, wing3, wing4 = butterfly
        move_butterfly(body, [wing1, wing2, wing3, wing4])
