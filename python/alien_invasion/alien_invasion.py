"""Look at this, is a game about aliens."""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Class for manage resources of game."""

    def __init__(self):
        """Init game and make game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
       # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
       # !Man, in a fullscreen moving object drop pixels, and CPU culler is UP.
       # self.settings.screen_width = self.screen.get_rect().width
       # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set background color. Default is black.
       # self.bg_color = (230, 230, 230)  # light gray color
        # RGB (255, 0, 0) - red
        #     (0, 255, 0) - green
        #     (0, 0, 255) - blue

    def run_game(self):
        """Start game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Handle press buttons of keyboard."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reaction for pressing buttons."""
        if event.key == pygame.K_RIGHT:
           #self.ship.rect.x += 1  # for one pixel to right
           self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reaction for unpressing buttons."""
        if event.key == pygame.K_RIGHT:
        #   self.ship.rect.x -= 1  # for one pixel to left
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Make a new bullet and include it to the group bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and remove an old bullets."""
        self.bullets.update()

        # Remove bullets after brink of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
       # print(len(self.bullets))  # show in terminal how bullets in a game

    def _create_fleet(self):
        """Make fleet of aliens."""
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        """Update rectangle and show new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # make an exemplar and start the game
    ai = AlienInvasion()
    ai.run_game()
