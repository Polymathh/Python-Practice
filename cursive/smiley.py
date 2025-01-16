import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_smiley():
    # Set up the turtle environment
    turtle.speed(3)
    turtle.bgcolor("white")
    
    # Draw the face
    draw_circle("yellow", 0, 0, 150)
    
    # Draw the left eye
    draw_circle("black", -60, 80, 20)

    
    # Draw the right eye
    draw_circle("black", 60, 80, 20)

    
    # Draw the mouth
    turtle.penup()
    turtle.goto(-75, -40)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.pensize(5)
    turtle.circle(90, 120)  # Draw an arc for the smile

    # Hide the turtle
    turtle.hideturtle()
    turtle.done()

# Call the function to draw the smiley
draw_smiley()
