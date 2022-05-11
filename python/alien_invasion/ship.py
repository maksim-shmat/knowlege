"""File for game alien_invasion. Backend for picture 'ship.png'."""

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class for manage the ship."""

    def __init__(self, ai_game):
        """Init ship and make a start position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        #self.x = float(self.rect.x)  # for exactly value
        self.moving_right = False
        self.moving_left = False
        # Load image of ship and get the rectangle.
        self.image = pygame.image.load('/home/jack/django2/knowlege/python/alien_invasion/images/ship2.png')
        self.rect = self.image.get_rect()
        # Every new ship will be appeared in a bottom line of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        """Update the ship position with True/False triger."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
#            self.x += self.settings.ship_speed
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
           # self.x -= self.settings.ship_speed
            self.rect.x -= 1
       # self.rect.x = self.x

    def blitme(self):
        """Design the ship in a current position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Put ship in the centre of bottom of the creen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
