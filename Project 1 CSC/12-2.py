import pygame
import sys

class GameCharacter:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self, screen, screen_rect):
        self.rect.center = screen_rect.center
        screen.blit(self.image, self.rect)

def main():
    pygame.init()

    screen_width = 800
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game Character")

    BACKGROUND_COLOR = (135, 206, 250)  # Sky Blue
    character = GameCharacter("char.png")
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BACKGROUND_COLOR)
        character.draw(screen, screen.get_rect())

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
