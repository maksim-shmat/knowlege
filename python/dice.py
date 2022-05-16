"""Dice model for matplotlib and plotly."""

from random import randint


class Dice():
    """Class is it be a dice."""
    def __init__(self, num_sides=6):
        """Sixsided dice(D6) as a default."""
        self.num_sides = num_sides

    def roll(self):
        """Return random number from 1 to amount of sides of dice."""
        return randint(1, self.num_sides)

