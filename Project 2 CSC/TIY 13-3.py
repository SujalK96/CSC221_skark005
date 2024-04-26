import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + randint(-10, 10)
        self.rect.y = self.rect.height + randint(-10, 10)

    def update(self):
        self.rect.y += self.settings.raindrop_speed

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.raindrop_speed = 0.5

class RaindropsGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")
        self.raindrops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        while True:
            self._check_events()
            self.raindrops.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_drops(self):
        drop = Raindrop(self.screen, self.settings)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - drop_width
        number_drops_x = available_space_x // (2 * drop_width)
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * drop_height)
        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        drop = Raindrop(self.screen, self.settings)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = drop_width + 2 * drop_width * drop_number + randint(-10, 10)
        drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number + randint(-10, 10)
        self.raindrops.add(drop)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    rd_game = RaindropsGame()
    rd_game.run_game()
