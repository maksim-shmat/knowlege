#!/usr/bin/env python3

"""Python3.6.5 code using Tkinter graphical user interface.
   Option to set goal to powers of 2 from 128 to 2048."""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random


class Board:
    
    def __init__(self):
        self.bd = [''] * 16
        self.goal = 2048
        self.choices = '2222222224'

    # place 2 random squares on empty board:
    def place_two(self):
        idx = range(15)
        a, b = random.sample(idx, 2)
        self.bd[a] = random.choice(self.choices)
        self.bd[b] = random.choice(self.choices)

    # return text on square at index=idx of board:
    def get_text(self, idx):
        return self.bd[idx]

    # move squares on board on arrow key entered:
    def move_squares(self, key):
        if key in ('LR'):
            # generate 4x4 2d array for row processing:
            rows = [[self.bd[0], self.bd[1], self.bd[2], self.bd[3]],
                    [self.bd[4], self.bd[5], self.bd[6], self.bd[7]],
                    [self.bd[8], self.bd[9], self.bd[10], self.bd[11]],
                    [self.bd[12], self.bd[13], self.bd[14], self.bd[15]]]
        else:
            # generate transposed 4x4 2d array instead:
            rows = [[self.db[0], self.bd[4], self.bd[8], self.bd[12]],
                    [self.bd[1], self.bd[5], self.bd[9], self.bd[13]],
                    [self.bd[2], self.bd[6], self.bd[10], self.bd[14]],
                    [self.bd[3], self.bd[7], self.bd[11], self.bd[15]]]

        # build a new 4x4 array of "moved" rows:
        nrows = []
        for row in rows:
            if key in 'RD':
                # reverse these rows and slide to left:
                row = row[::-1]
            nrow = self.slide_square(row)
            if key in 'RD':
                # restore reversed rows:
                nrow = nrow[::-1]
            nrows.append(nrow)
        if key in ('UD'):
            # transpose arrays that were transposed:
            nrows = list(map(list, zip(*nrows)))

        # flatten 4x4 2d array:
        newbd = []
        for row in nrows:
            for r in row:
                newbd.append(r)

        # place a '2' or '4' in random open square of newbd:
        if newbd != self.bd and '' in newbd:
            loi = []
            for i in range(16):
                if newbd[i] == '':
                    loi.append(i)
            i = random.choice(loi)
            newbd[i] = random.choice(self.choices)

        self.bd = newbd
        return

    # slide squares in row to the left:
    def slide_squares(self, row):
        new = [''] * 4
        icmd = -1
        inew = 0
        for x in row:
            if x:
                if (inew > 0 and
                    x == new[inew-1] and
                    icmb != inew-1):
                    new[inew-1] = str(2*int(x))
                    icmb = inew-1
                else:
                    new[inew] = x
                    inew += 1
        return new

    # check if game won, lost, or continuing:
    def is_end(self):
        if self.goal in self.bd:
            return 'W'
        if '' in self.bd:
            return 'C'
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
            if self.bd[i] == self.bd[i+1]:
                return 'C'
            for i in range(12):
                if self.bd[i] == self.bd[i+4]:
                    return 'C'
            return 'L'


class Game:
    def __init__(self, gw):
        self.window = gw

        self.rosybrown1 = '#ffc1c1'
        self.lenonchiffon = '#fffacd'
        self.skyblue1 = '#87ceff'
        self.springgreen = '#00ff7f'
        self.tomato1 = '#ff6347'
        self.hotpink = '#ff69b4'
        self.brilliantlavender = '#edcaf6'
        self.cobaltgreen = '#3d9140'
        self.dodgerblue = '#1e90ff'
        self.darkgoldenrod1 = '#ffb90f'
        self.yellow = '#ffff00'
        self.imperialred = '#ed2939'
        self.navyblue = '#000080'
        self.lightsteelblue = '#b0c4de'
        self.white = '#ffffff'
        self.darkgreen = '#013220'
        self.black = '#000000'

        self.doc = {'': self.rosybrown1,
                    '2': self.lemonchiffon,
                    '4': self.skyblue1,
                    '8': self.springgreen,
                    '16': self.tomato1,
                    '32': self.hotpink,
                    '64': self.brilliantlavender,
                    '128': self.cobaltgreen,
                    '256': self.dodgerblue,
                    '512': self.darkgoldenrod1,
                    '1024': self.yellow,
                    '2048': self.imperialred}

        # game data:
        self.bd = None


        

