"""Abelian sands problem with tkinter."""

from tkinter import *

# given a grid, display it on a tkinter Canvas:
class Sandpile:
    def __init__(self, wn, grid):
        self.window = wn
        self.grid = grid
        self.canvas = Canvas(wn, bg='lemon chiffon')
        self.canvas.pack(fill=BOTH, expand=1)

        colors = {0: 'dodger blue',
                  1: 'red',
                  2: 'green',
                  3: 'lemon chiffon'}

        x = 10
        y = 10
        d = 5

        for row in self.grid:
            for value in row:
                clr = colors[value]
                self.canvas.create_rectangle(
                        x, y, x+d, y+d,
                        outline=clr,
                        fill=clr)
                x += 5
            x = 10
            y += 5


class Grid:
    def __init__(self, size, center):
        self.size = size      # rows/cols in (best if odd)
        self.center = center  # start value at center of grid
        self.grid = [[0]*self.size for i in range(self.size)]
        self.grid[self.size // 2][self.size // 2] = self.center

    def show(self, msg):
        '''Print the grid.'''
        print('  ' + msg + ':')
        for row in self.grid:
            print(' '.join(str(x) for x in row))
        print()
        return

    def abelian(self):
        '''Dissipate piles of sand as required.'''
        while True:
            found = False
            for r in range(self.size):
                for c in range(self.size):
                    if self.grid[r][c] > 3:
                        self.distribute(self.grid[r][c], r, c)
                        found = True
            if not found:
                return

    def distribute(self, nbr, row, col):
        '''distribute sand from a single pile to its neighbors.'''
        qty, remain = divmod(nbr, 4)
        self.grid[row][col] = remain
        for r, c in [(row+1, col),
                     (row-1, col),
                     (row, col+1),
                     (row, col-1)]:
            self.grid[r][c] += qty
        return

    def display(self):
        '''Display the grid using tkinter.'''
        root = Tk()
        root.title('Sandpile')
        root.geometry('700x700+100+50')
        sp = Sandpile(root, self.grid)
        root.mainloop()

# execute program for size, center value pair:
# just print results for a small grid
g = Grid(9, 17)
g.show('BEFORE')
g.abelian()  # scatter the sand
g.show('AFTER')

# just show results in tkinter for a large grid
# I wish there was a way to attach a screen shot
# of the tkinter result here
g = Grid(131,25000)
g.abelian()  # scatter the sand
g.display()  # display result using tkinter

