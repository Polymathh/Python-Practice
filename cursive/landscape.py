import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Turtle Landscape")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)

# Create a turtle object
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Function to draw a rectangle
def draw_rectangle(color, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a triangle
def draw_triangle(color, x, y, base, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x + base / 2, y + height)
    t.goto(x + base, y)
    t.goto(x, y)
    t.end_fill()

# Function to draw a circle
def draw_circle(color, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw the grass
draw_rectangle("green", -400, -100, 800, 200)

# Draw the sun
draw_circle("yellow", 300, 200, 60)

# Draw a tree trunk
draw_rectangle("brown", -250, -100, 30, 100)

# Draw tree leaves (three circles stacked)
draw_circle("darkgreen", -235, 50, 50)
draw_circle("darkgreen", -235, 100, 40)
draw_circle("darkgreen", -235, 140, 30)

# Draw the house body
draw_rectangle("lightblue", -100, -100, 150, 100)

# Draw the house roof
draw_triangle("red", -125, 0, 200, 100)

# Draw the house door
draw_rectangle("brown", -60, -100, 40, 60)

# Draw the house windows
draw_rectangle("white", -90, -40, 30, 30)
draw_rectangle("white", -10, -40, 30, 30)

# Final touch: add some clouds
draw_circle("white", -200, 180, 30)
draw_circle("white", -170, 190, 40)
draw_circle("white", -130, 180, 30)

draw_circle("white", 0, 150, 30)
draw_circle("white", 30, 160, 40)
draw_circle("white", 70, 150, 30)

# Keep the window open
screen.mainloop()
