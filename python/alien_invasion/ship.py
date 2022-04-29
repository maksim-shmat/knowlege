"""File for game alien_invasion. Backend for picture 'ship.png'."""

import pygame

class Ship():
    """Class for manage the ship."""

    def __init__(self, ai_game):
        """Init ship and make a start position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load image of ship and get the rectangle.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Every new ship will be appeared in a bottom line of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Design the ship in a current position."""
        self.screen.blit(self.image, self.rect)
