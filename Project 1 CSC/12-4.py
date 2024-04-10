import pygame
import sys
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rocket Game")
rocket_img = pygame.image.load("rock.webp").convert_alpha()
rocket_width = 160
rocket_height = 160
rocket_img = pygame.transform.scale(rocket_img, (rocket_width, rocket_height))
rocket_x = (screen_width - rocket_width) // 2
rocket_y = (screen_height - rocket_height) // 2

rocket_speed = 8
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    # Move the rocket based on arrow key input
    if keys[pygame.K_UP] and rocket_y > 0:
        rocket_y -= rocket_speed
    if keys[pygame.K_DOWN] and rocket_y < screen_height - rocket_height:
        rocket_y += rocket_speed
    if keys[pygame.K_LEFT] and rocket_x > 0:
        rocket_x -= rocket_speed
    if keys[pygame.K_RIGHT] and rocket_x < screen_width - rocket_width:
        rocket_x += rocket_speed

    screen.fill((255, 255, 255))
    screen.blit(rocket_img, (rocket_x, rocket_y))
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()
