import pygame
 
class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen.get_rect().midleft
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
