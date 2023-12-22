import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_width = 50
player_height = 50
player_speed = 5
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10, player_width, player_height)

# Live bar
live_bar_width = 200
live_bar_height = 20
live_bar_color = (0, 255, 0)
live = live_bar_width

# Rockets
rocket_width = 50
rocket_height = 50
rocket_speed = 5
rockets = []

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Live Bar Game")
clock = pygame.time.Clock()

def draw_live_bar(live):
    pygame.draw.rect(screen, live_bar_color, (10, 10, live, live_bar_height))

def draw_player():
    pygame.draw.rect(screen, WHITE, player)

def draw_rockets():
    for rocket in rockets:
        pygame.draw.rect(screen, RED, rocket)

def move_rockets():
    for rocket in rockets:
        rocket.y += rocket_speed

def generate_rocket():
    x = random.randint(0, WIDTH - rocket_width)
    y = -rocket_height
    rockets.append(pygame.Rect(x, y, rocket_width, rocket_height))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player_width:
        player.x += player_speed

    screen.fill((0, 0, 0))

    draw_live_bar(live)
    draw_player()
    draw_rockets()

    move_rockets()

    # Check for collisions
    for rocket in rockets:
        if player.colliderect(rocket):
            live -= 10
            rockets.remove(rocket)

    # Generate new rockets
    if random.random() < 0.02:
        generate_rocket()

    if live <= 0:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(FPS)