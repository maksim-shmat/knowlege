"""Bullet for file alien_invasion.py"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets from ship."""

    def __init__(self, ai_game):
        """Make bullet object in a current position of ship."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Make bullet in the position (0,0) and go to right position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # bullet position in a float format
        self.y = float(self.rect.y)

    def update(self):
        """Go bullet to the bottom of screen."""
        # new bullet position in a float format
        self.y -= self.settings.bullet_speed
        # new rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """Show bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

