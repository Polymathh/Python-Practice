import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Pulley System Simulation")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Pulley wheel
pulley = turtle.Turtle()
pulley.hideturtle()
pulley.speed(0)
pulley.pensize(3)

# Rope
rope = turtle.Turtle()
rope.hideturtle()
rope.speed(0)
rope.pensize(3)

# Load
load = turtle.Turtle()
load.shape("square")
load.color("red")
load.penup()
load.shapesize(stretch_wid=2, stretch_len=2)

# Draw pulley wheel
def draw_pulley():
    pulley.penup()
    pulley.goto(0, 150)
    pulley.pendown()
    pulley.circle(50)

# Draw rope
def draw_rope(y_offset):
    rope.clear()
    rope.penup()
    rope.goto(0, 150)  # Top center of the pulley
    rope.pendown()
    rope.goto(0, 150 - y_offset)  # Rope to the load
    rope.penup()
    rope.goto(0, 150)  # Back to top
    rope.pendown()
    rope.goto(200, 150)  # Rope to the side

# Simulate the pulley
def simulate_pulley():
    load_y = -50  # Initial position of the load
    while True:
        for _ in range(50):
            # Move load up
            load_y += 2
            load.goto(0, load_y)
            draw_rope(load_y + 200)  # Adjust rope with load movement
            time.sleep(0.05)
            screen.update()

        for _ in range(50):
            # Move load down
            load_y -= 2
            load.goto(0, load_y)
            draw_rope(load_y + 200)  # Adjust rope with load movement
            time.sleep(0.05)
            screen.update()

# Main program
draw_pulley()
simulate_pulley()
