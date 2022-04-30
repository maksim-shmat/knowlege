"""Look at this, is a game about aliens."""

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class for manage resources of game."""

    def __init__(self):
        """Init game and make game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(screen)  # ! Not attribute screen. And where it is?

        # Set background color. Default is black.
       # self.bg_color = (230, 230, 230)  # light gray color
        # RGB (255, 0, 0) - red
        #     (0, 255, 0) - green
        #     (0, 0, 255) - blue

    def run_game(self):
        """Start game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Handle press buttons of keyboard."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update rectangle and show new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # make an exemplar and start the game
    ai = AlienInvasion()
    ai.run_game()
