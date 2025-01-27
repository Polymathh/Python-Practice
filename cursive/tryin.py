import turtle
import colorsys

def draw_colorful_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    spiral = turtle.Turtle()
    spiral.speed(0)
    spiral.width(2)

    # Total number of colors in the spiral
    num_colors = 360
    hue = 0  # Starting color hue

    for i in range(num_colors * 2):
        # Set the color using HSV to RGB conversion
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        spiral.color(color)

        # Draw the spiral
        spiral.forward(i * 2)
        spiral.right(59)
        hue += 1 / num_colors  # Increment hue to change color gradually

    spiral.hideturtle()
    screen.mainloop()

draw_colorful_spiral()
