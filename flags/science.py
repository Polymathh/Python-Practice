import turtle

def draw_text(message, x, y, font_size, color):
    """Draws text on the screen at a specified position."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(message, align="center", font=("Arial", font_size, "bold"))
    turtle.pendown()

def draw_heart():
    """Draws a red heart."""
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(100)
    turtle.circle(50, 180)
    turtle.right(90)
    turtle.circle(50, 180)
    turtle.forward(100)
    turtle.end_fill()

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("I ♥ SCIENCE")

    # Draw the "I"
    draw_text("I", -200, 100, 40, "white")

    # Draw the heart
    draw_heart()

    # Draw "SCIENCE"
    draw_text("SCIENCE", 200, 100, 40, "white")

    # Finish
    turtle.hideturtle()
    screen.mainloop()

main()
