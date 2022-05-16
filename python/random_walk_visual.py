"""Random walk for matplotlib, from random_walk.py."""

import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    # Build the random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Put points on the diagramm
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16, 9), dpi=96)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none', s=4)
    #ax.scatter(rw.x_values, rw.y_values, s=15)
    # Header first and last point
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100)
    # Remove axis, if it needed for good visual
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
