"""Look at this, is a game about aliens."""

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        # Make an exemplar for save statistics
        # and panel of results(scoreboard)
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

            # Set background color. Default is black.
            # self.bg_color = (230, 230, 230)  # light gray color
            # RGB (255, 0, 0) - red
            #     (0, 255, 0) - green
            #     (0, 0, 255) - blue
        
        # Make a Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game aftef press in "Play" button."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            # Clear lists of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Make new fleet and put the ship on the center of the screen
            self._create_fleet()
            self.ship.center_ship()

            # Hide cursor
            pygame.mouse.set_visible(False)

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
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Handling collisions bullets with targets."""
            # check collide bullet with target
            # if collide checked that remove bullet and target
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
            # or False, True for cumulative effect
        if not self.aliens:
                # Make a new fleet and remove existed bullets
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _create_fleet(self):
        """Make fleet of aliens."""
            # make an alien and count how many aliens in a row
            # interval between aliens equals one width of alien
        alien = Alien(self)
        alien_width, alien_height  = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Count how many rows may be on the screen."""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

            # Make a fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
            # Make an alien and put her in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """React to the touch, if alien on the brink or screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Descend all fleet and move to the backward."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _ship_hit(self):
        """Handle collide ship and alien."""
        if self.stats.ships_left > 0:
                # Decrease ships_left
            self.stats.ships_left -= 1
                # Clear list of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
                # Create new fleet and put ship in a centre
            self._create_fleet()
            self.ship.center_ship()
                # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Does alien goes to the bottom of the screen?"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # doubled reaction how target collide with ship
                self._ship_hit()
#                break

    def _update_aliens(self):
        """Update position of all aliens into the fleet after 
        fleet is moved to the brink of screen."""
        self._check_fleet_edges()
        self.aliens.update()

            # check collisions "target-ship".
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("Ship hit!!!")  # message on the terminal
            self._ship_hit()

            # check, if aliens goes to the bottom of the screen
        self._check_aliens_bottom()
         


    def _update_screen(self):
        """Update rectangle and show new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Return info score about
        self.sb.show_score()

        # Show Play button if game not active
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # make an exemplar and start the game
    ai = AlienInvasion()
    ai.run_game()
