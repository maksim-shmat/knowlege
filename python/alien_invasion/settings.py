"""Settings for game Alien Invasion."""

class Settings():
    """Class for all game settings."""

    def __init__(self):
        """Init game settings."""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship params
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet parameters
        self.bullet_speed = 1  # if value higher you make a more burden on sys
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # only three bullet in the game

        # Alien parametes
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
       # fleet_direction = 1 is mean a move to right, and -1 to left
        self.fleet_direction = 1

        # Speed up of game
        self.speedup_scale = 1.1  # if value 1 - speed not higher,
                                  # if value 2 - speed x2 in a new step
        # Speed for growth of alien's score weight
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings how changed through the game process."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 means moves to the left, and -1 to the right.
        self.fleet_direction = 1

        # count scores
        self.alien_points = 50

    def increase_speed(self):
        """Settings for increase of speed and score weight of aliens."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    
