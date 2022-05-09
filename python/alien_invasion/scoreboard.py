"""Count the score for alien_invasion.py."""

import pygame.font


class Scoreboard():
    """Class for returning game info."""

    def __init__(self, ai_game):
        """Init atributes for count of scores."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Settings for fonts of score.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Preposition of start image for score
        self.prep_score()

    def prep_score(self):
        """Make currently score into graphical image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Return score to the right-up side of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Return score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
