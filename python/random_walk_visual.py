"""Random walk for matplotlib, from random_walk.py."""

import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    # Build the random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Put points on the diagramm
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
