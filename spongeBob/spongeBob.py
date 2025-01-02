import turtle


def draw_rectangle(color, x, y, width, height):
    """Draw a filled rectangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_circle(color, x, y, radius):
    """Draw a filled circle."""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_spongebob():
    # Draw body
    draw_rectangle("yellow", -100, -100, 200, 300)

    # Draw eyes
    draw_circle("white", -50, 150, 30)
    draw_circle("white", 50, 150, 30)
    draw_circle("blue", -50, 150, 15)
    draw_circle("blue", 50, 150, 15)
    draw_circle("black", -50, 150, 7)
    draw_circle("black", 50, 150, 7)

    # Draw mouth
    draw_rectangle("black", -60, 60, 120, 10)

    # Draw pants
    draw_rectangle("brown", -100, -100, 200, 50)
    draw_rectangle("white", -100, -50, 200, 10)

    # Draw legs
    draw_rectangle("yellow", -60, -150, 20, 50)
    draw_rectangle("yellow", 40, -150, 20, 50)

    # Draw shoes
    draw_rectangle("black", -65, -200, 30, 20)
    draw_rectangle("black", 35, -200, 30, 20)

    # Draw arms
    draw_rectangle("yellow", -160, 80, 60, 20)  # Left arm
    draw_rectangle("yellow", 100, 80, 60, 20)  # Right arm

    # Thumbs up (right hand)
    draw_rectangle("yellow", 160, 80, 20, 50)  # Thumb
    draw_circle("yellow", 170, 140, 10)        # Thumb tip


def display_text():
    """Display the text 'SpongeBob' below the character."""
    turtle.penup()
    turtle.goto(0, -250)  # Position below the figure
    turtle.color("yellow")
    turtle.write("SpongeBob", align="center", font=("Comic Sans MS", 40, "bold"))


# Setup Turtle
turtle.speed(5)
turtle.bgcolor("skyblue")

# Draw SpongeBob-inspired character
draw_spongebob()

# Display text
display_text()

# Finish
turtle.hideturtle()
turtle.done()
