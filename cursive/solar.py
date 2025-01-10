import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System")
screen.setup(width=1000, height=1000)

# Create the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)
sun.penup()

# Display "Solar System" title
title_pen = turtle.Turtle()
title_pen.hideturtle()
title_pen.color("white")
title_pen.penup()
title_pen.goto(0, 400)
title_pen.write("Solar System", align="center", font=("Arial", 24, "bold"))

# Create planets
class Planet(turtle.Turtle):
    def __init__(self, color, size, distance, speed, name):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.shapesize(size)
        self.penup()
        self.distance = distance
        self.speed = speed
        self.angle = 0
        self.name = name
        self.label = turtle.Turtle()  # Turtle for the label
        self.label.hideturtle()
        self.label.color("white")
        self.label.penup()
        self.goto(self.distance, 0)

    def update_label(self):
        self.label.goto(self.xcor() + 10, self.ycor() + 10)
        self.label.clear()
        self.label.write(self.name, align="center", font=("Arial", 10, "bold"))

# Initialize planets (name, color, size, distance from sun, orbit speed)
planets = [
    Planet("gray", 0.4, 60, 4.8, "Mercury"), 
    Planet("orange", 0.6, 100, 3.5, "Venus"),  
    Planet("blue", 0.8, 140, 3, "Earth"),  
    Planet("red", 0.5, 180, 2.5, "Mars"), 
    Planet("brown", 1.2, 240, 2, "Jupiter"),  
    Planet("yellow", 1.0, 300, 1.6, "Saturn"), 
    Planet("light blue", 0.9, 360, 1.2, "Uranus"), 
    Planet("blue", 0.9, 420, 1, "Neptune"), 
]

# Animation loop
while True:
    for planet in planets:
        planet.angle += planet.speed
        x = planet.distance * math.cos(math.radians(planet.angle))
        y = planet.distance * math.sin(math.radians(planet.angle))
        planet.goto(x, y)
        planet.update_label()
    time.sleep(0.02)

screen.mainloop()
