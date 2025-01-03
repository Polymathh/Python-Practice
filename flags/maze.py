import turtle

def draw_maze():
    """Draws a more complex maze using turtle graphics."""
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Turtle Maze")

    turtle.speed(0)
    turtle.color("white")
    turtle.pensize(2)

    # Define the maze structure (start_x, start_y, length, orientation)
    maze_walls = [
        (-300, 300, 600, "horizontal"),  # Outer boundary
        (-300, -300, 600, "horizontal"),
        (-300, 300, 600, "vertical"),
        (300, 300, 600, "vertical"),

        # Inner walls
        (-250, 250, 100, "horizontal"),
        (-250, 200, 400, "horizontal"),
        (50, 250, 200, "horizontal"),
        (-250, 150, 300, "horizontal"),
        (100, 150, 200, "horizontal"),
        (-200, 100, 300, "horizontal"),
        (50, 100, 250, "horizontal"),
        (-250, 50, 500, "horizontal"),
        (-150, 0, 200, "horizontal"),
        (100, 0, 100, "horizontal"),
        (-250, -50, 400, "horizontal"),
        (-200, -100, 150, "horizontal"),
        (50, -100, 250, "horizontal"),
        (-250, -150, 500, "horizontal"),
        (-250, -200, 200, "horizontal"),
        (0, -200, 300, "horizontal"),

        # Vertical walls
        (-250, 250, 500, "vertical"),
        (-200, 200, 300, "vertical"),
        (-150, 150, 500, "vertical"),
        (-100, 50, 500, "vertical"),
        (-50, 200, 200, "vertical"),
        (0, 150, 400, "vertical"),
        (50, 50, 600, "vertical"),
        (100, 250, 400, "vertical"),
        (150, 200, 300, "vertical"),
        (200, 250, 500, "vertical"),
        (250, 200, 400, "vertical"),
    ]

    # Draw the maze walls
    for x, y, length, orientation in maze_walls:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        if orientation == "horizontal":
            turtle.setheading(0)  # Draw horizontally
        else:
            turtle.setheading(270)  # Draw vertically
        turtle.forward(length)

    # Add entrance and exit
    turtle.penup()
    turtle.goto(-300, -275)  # Entrance
    turtle.pendown()
    turtle.color("green")
    turtle.setheading(0)
    turtle.forward(25)

    turtle.penup()
    turtle.goto(275, 300)  # Exit
    turtle.pendown()
    turtle.color("red")
    turtle.setheading(270)
    turtle.forward(25)

    # Finish up
    turtle.hideturtle()
    screen.mainloop()

draw_maze()
