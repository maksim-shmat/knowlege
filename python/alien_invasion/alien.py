"""File for main game file alien_invasion.py."""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """One alien example."""

    def __init__(self, ai_game):
        """Init alien and her position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load image of alien and make rect attribute
        self.image = pygame.image.load('images/mom.jpg')
        self.rect = self.image.get_rect()

        # Every new alien will be appeared in a left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save exactly position of alien
        self.x = float(self.rect.x)
