"""Look at this, is a game about aliens."""

import sys
import pygame

class AlienInvasion:
    """Class for manage resources of game."""

    def __init__(self):
        """Init game and make game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start game."""
        while True:
            # Check keyboard.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Shoe the last generated screen
            pygame.display.flip()

if __name__ == '__main__':
    # make an exemplar and start the game
    ai = AlienInvasion()
    ai.run_game()
