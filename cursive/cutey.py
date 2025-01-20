import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("😍 Emoji")

# Create turtles for each part
face = turtle.Turtle()
hearts = turtle.Turtle()
smile = turtle.Turtle()

# Set speeds
face.speed(1)
hearts.speed(1)
smile.speed(1)

# Draw a circle for the face
def draw_face():
    face.penup()
    face.goto(0, -200)  # Start from bottom of the circle
    face.pendown()
    face.fillcolor("#FFD700")  # Gold color
    face.begin_fill()
    face.circle(200)  # Circle radius
    face.end_fill()
    time.sleep(0.5)  # Pause to show the face

# Draw heart-shaped eyes
def draw_heart(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.left(50)
    t.forward(size)
    t.circle(size / 2, 180)
    t.right(100)
    t.circle(size / 2, 180)
    t.forward(size)
    t.end_fill()
    t.setheading(0)
    time.sleep(0.5)  # Pause after each heart

def draw_eyes():
    # Left heart eye
    draw_heart(hearts, -70, 70, 50)
    # Right heart eye
    draw_heart(hearts, 70, 70, 50)

# Draw the smile
def draw_smile():
    smile.penup()
    smile.goto(-100, -50)  # Start point of the smile
    smile.setheading(-60)
    smile.width(5)
    smile.pendown()
    smile.pencolor("black")
    smile.circle(120, 120)  # Draw an arc for the smile
    time.sleep(0.5)  # Pause after the smile

# Main drawing function
def draw_emoji_step_by_step():
    draw_face()
    draw_eyes()
    draw_smile()

# Run the drawing
draw_emoji_step_by_step()

# Keep the window open
screen.mainloop()

