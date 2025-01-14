import turtle

# Initialize the screen
screen = turtle.Screen()
screen.title("Manchester United Inspired Emblem")
screen.bgcolor("white")

# Create the turtle object
artist = turtle.Turtle()
artist.speed(10)

# Function to draw a circle
def draw_circle(color, x, y, radius):
    artist.penup()
    artist.goto(x, y - radius)  # Adjust for turtle's starting position
    artist.pendown()
    artist.color(color)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()

# Function to write text
def write_text(message, font_size, color, x, y):
    artist.penup()
    artist.goto(x, y)
    artist.color(color)
    artist.write(message, align="center", font=("Arial", font_size, "bold"))
    artist.pendown()

# Draw outer circle (red)
draw_circle("red", 0, 0, 200)

# Draw inner yellow circle
draw_circle("yellow", 0, 0, 160)

# Write "MANCHESTER" on top
write_text("MANCHESTER", 24, "red", 0, 130)

# Write "UNITED" at the bottom
write_text("UNITED", 24, "red", 0, -170)

# Draw a soccer ball in the middle
def draw_soccer_ball(x, y, size):
    artist.penup()
    artist.goto(x, y)
    artist.color("black")
    artist.pendown()

    # Outer circle
    artist.begin_fill()
    artist.circle(size)
    artist.end_fill()

    # Add pentagon patterns
    artist.penup()
    artist.goto(x, y + size)
    artist.color("white")
    artist.pendown()

    for _ in range(6):
        artist.forward(size * 1.5)
        artist.right(120)

# Place the soccer ball in the middle
draw_soccer_ball(0, -30, 30)

# Create decorative rectangles
def draw_rectangle(color, x, y, width, height):
    artist.penup()
    artist.goto(x, y)
    artist.color(color)
    artist.pendown()
    artist.begin_fill()
    for _ in range(2):
        artist.forward(width)
        artist.left(90)
        artist.forward(height)
        artist.left(90)
    artist.end_fill()

# Decorative yellow bars
draw_rectangle("yellow", -150, 50, 300, 20)  # Top bar
draw_rectangle("yellow", -150, -70, 300, 20)  # Bottom bar

# Complete drawing
artist.hideturtle()

# Keep the screen open
screen.mainloop()
