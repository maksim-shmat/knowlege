"""File for main game file alien_invasion.py."""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """One alien example."""

    def __init__(self, ai_game):
        """Init alien and her position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load image of alien and make rect attribute
        self.image = pygame.image.load('images/mom.jpg')
        self.rect = self.image.get_rect()

        # Every new alien will be appeared in a left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save exactly position of alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True, if alien on the brink the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moving aliens to the right or left sides."""
        self.x += (self.settings.alien_speed *
                self.settings.fleet_direction)
        self.rect.x = self.x
