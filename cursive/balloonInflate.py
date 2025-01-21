import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Inflation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Balloon properties
balloon_x = WIDTH // 2
balloon_y = HEIGHT // 2
balloon_radius = 30
balloon_growth = 5  # Amount the balloon grows per keypress
max_radius = 200  # Maximum size before the balloon pops

# Fonts
font = pygame.font.SysFont("comicsansms", 40)

# Load pop sound
pop_sound = pygame.mixer.Sound(pygame.mixer.Sound(pygame.mixer.Sound(pygame.mixer.Sound('pop-94319.mp3'))))  
# You need to download a pop sound file named "pop.wav" and put it in the same folder as the script.

# Game loop
clock = pygame.time.Clock()

def show_message(text, color, size, y_offset=0):
    """Display a message on the screen."""
    font = pygame.font.SysFont("comicsansms", size)
    message = font.render(text, True, color)
    text_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(message, text_rect)

running = True
popped = False

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Inflate the balloon
        if event.type == pygame.KEYDOWN and not popped:
            if event.key == pygame.K_SPACE:
                balloon_radius += balloon_growth
                if balloon_radius >= max_radius:
                    popped = True
                    pop_sound.play()

    # Draw the balloon
    if not popped:
        pygame.draw.circle(screen, RED, (balloon_x, balloon_y), balloon_radius)
        show_message("Press SPACE to inflate", BLACK, 30, y_offset=200)
    else:
        show_message("POP!", RED, 60)
        show_message("The balloon popped!", BLACK, 40, y_offset=60)
        show_message("Press ESC to exit", BLACK, 30, y_offset=100)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
