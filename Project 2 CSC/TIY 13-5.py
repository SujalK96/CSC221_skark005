import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('rocket.jpeg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.speed_factor = 1.5
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.right = self.screen_rect.right
        self.rect.y = randint(0, self.settings.screen_height - self.rect.height)
        self.x = float(self.rect.x)
        self.speed_factor = settings.alien_speed_factor

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1.0

class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")
        self.ship = Ship(self.screen)
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _update_aliens(self):
        self.aliens.update()
        for alien in self.aliens.copy():
            if alien.rect.right <= 0:
                self.aliens.remove(alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        alien = Alien(self.screen, self.settings)
        alien_height = alien.rect.height
        available_space_y = self.settings.screen_height - 2 * alien_height
        number_aliens_y = available_space_y // (2 * alien_height)
        for alien_number in range(number_aliens_y):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        alien = Alien(self.screen, self.settings)
        alien.rect.y = randint(0, self.settings.screen_height - alien.rect.height)
        alien.rect.x = self.settings.screen_width + 2 * alien.rect.width * alien_number
        alien.x = alien.rect.x
        self.aliens.add(alien)

if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()
