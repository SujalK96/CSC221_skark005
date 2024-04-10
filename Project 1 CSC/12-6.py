import pygame
import sys

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sideways Shooter")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ship_img = pygame.image.load("rock.webp").convert_alpha() 
ship_width = 150
ship_height = 150
ship_img = pygame.transform.scale(ship_img, (ship_width, ship_height))

ship_x = 50
ship_y = (screen_height - ship_height) // 2
ship_speed = 5
bullet_width = 10
bullet_height = 5
bullet_speed = 10
bullets = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([ship_x + ship_width, ship_y + (ship_height // 2)])  # Add new bullet position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_y > 0:
        ship_y -= ship_speed
    if keys[pygame.K_DOWN] and ship_y < screen_height - ship_height:
        ship_y += ship_speed
    for bullet in bullets:
        bullet[0] += bullet_speed
    screen.fill(WHITE)
    screen.blit(ship_img, (ship_x, ship_y))
    for bullet in bullets:
        pygame.draw.rect(screen, BLACK, (bullet[0], bullet[1], bullet_width, bullet_height))

    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()
sys.exit()
