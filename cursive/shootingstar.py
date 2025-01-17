import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Shooting Stars")
screen.tracer(0)  # Turn off automatic updates for smooth animation
screen.setup(width=800, height=600)

# Create the star turtle
star = turtle.Turtle()
star.hideturtle()
star.speed(0)
star.penup()

# Draw stars in the background
stars = []
for _ in range(100):
    star.goto(random.randint(-400, 400), random.randint(-300, 300))
    star.dot(random.randint(2, 6), "white")  # Randomly sized stars
    stars.append((star.xcor(), star.ycor()))

# Shooting star turtle
shooting_star = turtle.Turtle()
shooting_star.shape("circle")
shooting_star.color("yellow")
shooting_star.speed(0)
shooting_star.penup()
shooting_star.hideturtle()

def create_shooting_star():
    """Generates a shooting star at a random location."""
    shooting_star.goto(random.randint(-400, 400), random.randint(0, 300))
    shooting_star.showturtle()

def move_shooting_star():
    """Animates the shooting star."""
    for _ in range(50):  # Move in small steps
        x, y = shooting_star.pos()
        shooting_star.goto(x - 8, y - 5)  # Move diagonally
        shooting_star.shapesize(random.uniform(0.5, 1.5))  # Change size slightly
        screen.update()
        time.sleep(0.02)  # Small delay for smooth animation
    shooting_star.hideturtle()

def twinkle_effect():
    """Simulates a twinkling effect for background stars."""
    star_index = random.randint(0, len(stars) - 1)
    x, y = stars[star_index]
    star.goto(x, y)
    star.dot(random.randint(2, 6), random.choice(["white", "yellow", "blue", "pink"]))

# Main loop
while True:
    create_shooting_star()
    move_shooting_star()
    for _ in range(5):  # Twinkle 5 random stars
        twinkle_effect()
    screen.update()

screen.mainloop()
