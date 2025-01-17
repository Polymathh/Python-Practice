import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Chessboard with Movable Pieces")
screen.setup(width=800, height=800)
screen.tracer(0)

# Constants
TILE_SIZE = 80
COLORS = ["#F0D9B5", "#B58863"]
PIECE_COLOR = "black"

# Draw the chessboard
def draw_chessboard():
    for row in range(8):
        for col in range(8):
            x = col * TILE_SIZE - 320
            y = 320 - row * TILE_SIZE
            color = COLORS[(row + col) % 2]
            draw_square(x, y, color)

# Draw a single square
def draw_square(x, y, color):
    square = turtle.Turtle()
    square.penup()
    square.goto(x, y)
    square.shape("square")
    square.shapesize(TILE_SIZE / 20, TILE_SIZE / 20)  # 20 is default size
    square.fillcolor(color)
    square.stamp()

# Draw pieces as circles
def draw_pieces():
    for row, line in enumerate(initial_positions):
        for col, piece in enumerate(line):
            if piece != ".":
                x = col * TILE_SIZE - 280
                y = 280 - row * TILE_SIZE
                draw_circle(x, y, PIECE_COLOR)

# Draw a circle (for pieces)
def draw_circle(x, y, color):
    piece = turtle.Turtle()
    piece.penup()
    piece.goto(x, y)
    piece.shape("circle")
    piece.shapesize(TILE_SIZE / 40)  # Adjust size for the pieces
    piece.fillcolor(color)
    piece.stamp()

# Map chess notation to row/column indices
def chess_to_index(chess_pos):
    col = ord(chess_pos[0].lower()) - ord("a")
    row = 8 - int(chess_pos[1])
    return row, col

# Move a piece
def move_piece(start, end):
    global initial_positions
    start_row, start_col = chess_to_index(start)
    end_row, end_col = chess_to_index(end)

    if initial_positions[start_row][start_col] != ".":
        # Move the piece
        initial_positions[end_row][end_col] = initial_positions[start_row][start_col]
        initial_positions[start_row][start_col] = "."

        # Redraw the board
        screen.clear()
        draw_chessboard()
        draw_pieces()
    else:
        print("No piece at the starting position!")

# Initial board setup (only pawns for simplicity)
initial_positions = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

# Draw the initial board
draw_chessboard()
draw_pieces()

# Input loop
while True:
    screen.update()
    move = screen.textinput("Move Piece", "Enter your move (e.g., e2 to e4):")
    if move and " to " in move:
        start, end = move.split(" to ")
        move_piece(start, end)
    else:
        print("Invalid move! Format: e2 to e4")
