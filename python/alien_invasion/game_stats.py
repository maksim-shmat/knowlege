"""Statistics for file alien_invasions.py"""

class GameStats():
    """See statistics game about."""

    def __init__(self, ai_game):
        """Init statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Init stats, changeable in a game process."""
        self.ships_left = self.settings.ship_limit
