import turtle

def draw_kenyan_flag():
  """Draws the Kenyan flag using the Turtle graphics library."""

  # Set up the turtle and screen
  t = turtle.Turtle()
  t.speed(0)  # Fastest speed for drawing
  screen = t.getscreen()
  screen.bgcolor("white")

  # Define flag dimensions
  flag_width = 300
  flag_height = 200

  # Draw the black triangle
  t.fillcolor("black")
  t.begin_fill()
  t.penup()
  t.goto(-flag_width/2, -flag_height/2)
  t.pendown()
  t.forward(flag_width)
  t.left(135)
  t.forward(flag_width * (2**0.5))
  t.left(135)
  t.forward(flag_width)
  t.end_fill()

  # Draw the red stripe
  t.fillcolor("red")
  t.begin_fill()
  t.penup()
  t.goto(-flag_width/2, -flag_height/2)
  t.pendown()
  t.forward(flag_width)
  t.left(90)
  t.forward(flag_height/2)
  t.left(90)
  t.forward(flag_width)
  t.left(90)
  t.forward(flag_height/2)
  t.end_fill()

  # Draw the white stripe
  t.fillcolor("white")
  t.begin_fill()
  t.penup()
  t.goto(-flag_width/2, 0)
  t.pendown()
  t.forward(flag_width)
  t.left(90)
  t.forward(flag_height/2)
  t.left(90)
  t.forward(flag_width)
  t.left(90)
  t.forward(flag_height/2)
  t.end_fill()

  # Draw the black stripe
  t.fillcolor("black")
  t.begin_fill()
  t.penup()
  t.goto(-flag_width/2, flag_height/2)
  t.pendown()
  t.forward(flag_width)
  t.left(90)
  t.forward(flag_height/2)
  t.left(90)
  t.forward(flag_width)
  t.left(90)
  t.forward(flag_height/2)
  t.end_fill()

  # Draw the red stripe
  t.fillcolor("red")
  t.begin_fill()
  t.penup()
  t.goto(-flag_width/2, flag_height/2)
  t.pendown()
  t.left(45)
  t.forward(flag_width * (2**0.5))
  t.right(135)
  t.forward(flag_width)
  t.right(135)
  t.forward(flag_width * (2**0.5))
  t.end_fill()

  # Draw the Maasai shield and spears
  t.penup()
  t.goto(-flag_width/4, 0)
  t.pendown()
  t.fillcolor("gold")
  t.begin_fill()
  t.circle(20)
  t.end_fill()

  # Draw spears (simplified)
  t.penup()
  t.goto(-flag_width/4 + 20, 0)
  t.pendown()
  t.width(3)
  t.forward(30)
  t.penup()
  t.goto(-flag_width/4 - 20, 0)
  t.pendown()
  t.forward(30)

  # Hide the turtle
  t.hideturtle()

  # Keep the window open
  turtle.done()

if __name__ == "__main__":
  draw_kenyan_flag()