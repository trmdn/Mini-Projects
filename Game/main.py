import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

screen_width = 800
screen_height = 600

# SCREEN
show_screen = pygame.display.set_mode((screen_width, screen_height))

running = True

# SET CAPTION
pygame.display.set_caption("JUST A GAME")

# RUNNING SCREEN
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
