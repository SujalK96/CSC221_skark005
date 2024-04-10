import pygame
import sys

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Sky")

# Define colors
BLUE = (135, 206, 250)  # Sky Blue

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with blue
    screen.fill(BLUE)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
