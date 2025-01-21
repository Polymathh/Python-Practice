import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Swinging Pendulums with Collisions")
screen.tracer(0)

# Pendulum settings
num_pendulums = 5  # Number of pendulums
pendulum_length = 200  # Length of pendulums
angle_amplitude = 45  # Maximum swing angle in degrees
gravity = 0.005  # Gravity effect on the pendulum
damping = 0.99  # Damping factor to reduce energy over time

# Create pendulums
pendulums = []
velocities = []
angles = []

for i in range(num_pendulums):
    pendulum = turtle.Turtle()
    pendulum.shape("circle")
    pendulum.color("white")
    pendulum.penup()
    pendulum.goto(-150 + i * 100, 0)  # Horizontally spaced
    pendulum.pendown()
    pendulum.speed(0)
    pendulums.append(pendulum)
    velocities.append(0)  # Initial velocity
    angles.append((-1)**i * angle_amplitude)  # Alternate starting directions

# Draw lines to pendulums
lines = []
for pendulum in pendulums:
    line = turtle.Turtle()
    line.color("white")
    line.penup()
    line.goto(pendulum.xcor(), pendulum.ycor() + pendulum_length)
    line.pendown()
    line.goto(pendulum.xcor(), pendulum.ycor())
    line.hideturtle()
    lines.append(line)

# Simulation loop
while True:
    for i in range(num_pendulums):
        # Calculate pendulum dynamics
        acceleration = -gravity * math.sin(math.radians(angles[i]))
        velocities[i] += acceleration
        velocities[i] *= damping  # Damping effect
        angles[i] += velocities[i]

        # Update pendulum position
        x_offset = math.sin(math.radians(angles[i])) * pendulum_length
        y_offset = -math.cos(math.radians(angles[i])) * pendulum_length
        pendulums[i].setx(lines[i].xcor() + x_offset)
        pendulums[i].sety(lines[i].ycor() + y_offset)

        # Update the line
        lines[i].clear()
        lines[i].penup()
        lines[i].goto(lines[i].xcor(), lines[i].ycor() + pendulum_length)
        lines[i].pendown()
        lines[i].goto(pendulums[i].xcor(), pendulums[i].ycor())

    # Detect collisions
    for i in range(num_pendulums - 1):
        for j in range(i + 1, num_pendulums):
            distance = math.sqrt(
                (pendulums[i].xcor() - pendulums[j].xcor())**2 +
                (pendulums[i].ycor() - pendulums[j].ycor())**2
            )
            if distance < 20:  # Collision threshold
                # Swap velocities on collision
                velocities[i], velocities[j] = velocities[j], velocities[i]

    screen.update()
