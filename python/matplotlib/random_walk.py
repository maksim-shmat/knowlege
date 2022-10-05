"""Random walk for matplotlib and random_walk_visual.py."""

from random import choice


class RandomWalk():
    """Class for generate random walks."""

    def __init__(self, num_points=5000):
        """Init random walks athributes."""
        self.num_points = num_points

        # all walks start from point (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Count all points of walks."""

        # Steps generate before how len is needed
        while len(self.x_values) < self.num_points:

            # Which side is nedded to walk
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Steps on zero
            if x_step == 0 and y_step == 0:
                continue

            # Count next values of x and y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
