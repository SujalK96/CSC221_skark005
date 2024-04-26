import sys
import pygame
from pygame.sprite import Sprite
from random import randint

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BG_COLOR = (50, 50, 50)

class Star(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + randint(-10, 10)
        self.rect.y = self.rect.height + randint(-10, 10)

class StarsGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Stars")
        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_stars(self):
        star = Star(self.screen)
        star_width, star_height = star.rect.size
        available_space_x = SCREEN_WIDTH - star_width
        number_stars_x = available_space_x // (2 * star_width)
        available_space_y = SCREEN_HEIGHT - star_height
        number_rows = available_space_y // (2 * star_height)
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        star = Star(self.screen)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number + randint(-10, 10)
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number + randint(-10, 10)
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(BG_COLOR)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    sg = StarsGame()
    sg.run_game()
