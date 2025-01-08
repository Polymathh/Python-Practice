import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Text")
screen.setup(width=800, height=600)

# Create a turtle object
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)
pen.color("white")
pen.hideturtle()

# List of colors for a vibrant look
colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]

def draw_text(message, x, y, font_size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.choice(colors))  # Random color for each letter

    for letter in message:
        pen.write(letter, font=("Brush Script MT", font_size, "italic"))
        time.sleep(0.2)  # Pause for animation effect
        pen.penup()
        pen.forward(font_size)  # Move forward for the next letter
        pen.pendown()

def glow_effect(message, x, y, font_size, repetitions=5):
    for _ in range(repetitions):
        screen.bgcolor(random.choice(colors))  # Change background color
        pen.clear()
        draw_text(message, x, y, font_size)
        time.sleep(0.3)

# Main function
def main():
    message = "Hello TikTok!"  # Replace with your message or logo text
    x = -200  # Starting x-coordinate
    y = 0     # Starting y-coordinate
    font_size = 30  # Font size for the text

    # Glow effect
    glow_effect(message, x, y, font_size)

    # Final static message
    screen.bgcolor("black")
    pen.clear()
    pen.color("white")
    draw_text(message, x, y, font_size)

    # Keep the screen open
    screen.mainloop()

if __name__ == "__main__":
    main()
