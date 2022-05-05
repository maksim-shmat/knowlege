"""Settings for game Alien Invasion."""

class Settings():
    """Class for all game settings."""

    def __init__(self):
        """Init game settings."""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # Bullet parameters
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # only three bullet in the game

        # Alien parametes
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 is mean a move to right, and -1 to left
        self.fleet_direction = 1
