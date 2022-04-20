"""An alternative procedural approach in 100 prisoners probleb,

from 100_prisoners.py.
"""

# Procedural Python

import random

def main():
    NUM_DRAWERS = 100
    NUM_REPETITIONS = int(1E4) # 1e4(10_000), 1e5(100_000)

    print('{:15}: {:5} ({})'.format('approach', 'wins', 'ratio'))
    for approach in PrisonersGame.approaches:
        num_victories = 0
        for _ in range(NUM_REPETITIONS):
            game = PrisonersGame(NUM_DRAWERS)
            num_victories += PrisonersGame.victory(game.play(approach))

        print('{:15}: {:5} ({:.2%})'.format(
            approach.__name__, num_victories, num_victories / NUM_REPETITIONS))


class PrisonersGame:
    '''docstrings for PrisonersGame'''
    def __init__(self, num_drawers):
        assert num_drawers % 2 == 0
        self.num_drawers = num_drawers
        self.max_attempts = int(self.num_drawers / 2)
        self.drawer_ids = list(range(1, num_drawers + 1))
        shuffled = self.drawer_ids[:]
        random.shuffle(shuffled)
        self.drawers = dict(zip(self.drawer_ids, shuffled))

    def play_naive(self, player_number):
        '''Randomly open drawers'''
        for attempt in range(self.max_attempts):
            if self.drawers[random.choice(self.drawer_ids)] == player_number:
                return True
        return False

    def play_naive_mem(self, player_number):
        '''Randomly open drawers but avoiding repetitions'''
        not_attemped = self.drawer_ids[:]
        for attempt in range(self.max_attempts):
            guess = random.choice(not_attemped)
            not_attemped.remove(guess)

            if self.drawers[guess] == player_number:
                return True
        return False

    def play_optimum(self, player_number):
        '''Open the drawer that matches the player number and then open
        the drawer with the revealed number.
        '''
        prev_attempt = player_number
        for attempt in range(self.max_attempts):
            if self.drawers[prev_attempt] == player_number:
                return True
            else:
                prev_attempt = self.drawers[prev_attempt]
        return False

    @classmethod
    def victory(csl, results):
        '''Defines a victory of a game: all players won'''
        return all(results)

    approaches = [play_naive, play_naive_mem, play_optimum]

    def play(self, approach):
        '''Plays this game and returns a list of booleans with True
        if a player one , False otherwise'''
        return [approach(self, player) for player in self.drawer_ids]

if __name__ == '__main__':
    main()
