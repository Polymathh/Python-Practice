import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CAR_COLORS = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 165, 0)]

# Clock for managing FPS
clock = pygame.time.Clock()

# Traffic light class
class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED
        self.last_change_time = time.time()

    def update(self):
        current_time = time.time()
        # Change light every 5 seconds
        if self.color == RED and current_time - self.last_change_time > 5:
            self.color = GREEN
            self.last_change_time = current_time
        elif self.color == GREEN and current_time - self.last_change_time > 5:
            self.color = YELLOW
            self.last_change_time = current_time
        elif self.color == YELLOW and current_time - self.last_change_time > 2:
            self.color = RED
            self.last_change_time = current_time

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 50, 150))
        if self.color == RED:
            pygame.draw.circle(screen, RED, (self.x + 25, self.y + 25), 20)
        elif self.color == YELLOW:
            pygame.draw.circle(screen, YELLOW, (self.x + 25, self.y + 75), 20)
        elif self.color == GREEN:
            pygame.draw.circle(screen, GREEN, (self.x + 25, self.y + 125), 20)

# Car class
class Car:
    def __init__(self, x, y, speed, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction  # "horizontal" or "vertical"
        self.color = random.choice(CAR_COLORS)

    def move(self, traffic_light):
        if self.direction == "horizontal":
            if traffic_light.color == GREEN or self.x < traffic_light.x - 60:
                self.x += self.speed
        elif self.direction == "vertical":
            if traffic_light.color == GREEN or self.y < traffic_light.y - 60:
                self.y += self.speed

    def draw(self):
        if self.direction == "horizontal":
            pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 30))
        elif self.direction == "vertical":
            pygame.draw.rect(screen, self.color, (self.x, self.y, 30, 50))

# Initialize objects
traffic_light = TrafficLight(WIDTH // 2 - 25, HEIGHT // 2 - 75)
cars = [Car(random.randint(-400, -50), HEIGHT // 2 + 50, random.randint(2, 4), "horizontal") for _ in range(5)]
cars += [Car(WIDTH // 2 + 50, random.randint(-400, -50), random.randint(2, 4), "vertical") for _ in range(5)]

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update traffic light
    traffic_light.update()
    traffic_light.draw()

    # Update and draw cars
    for car in cars:
        car.move(traffic_light)
        car.draw()

    # Reset cars when they leave the screen
    for car in cars:
        if car.direction == "horizontal" and car.x > WIDTH:
            car.x = random.randint(-400, -50)
            car.y = HEIGHT // 2 + 50
        elif car.direction == "vertical" and car.y > HEIGHT:
            car.y = random.randint(-400, -50)
            car.x = WIDTH // 2 + 50

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
