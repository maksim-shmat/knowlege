"""Eight Queens problem about."""

#1
def conflict(state, nextX):  # nextX - horizontal position
   nextY = len(state)
   for i in range(nextY):  # nextY - vertical position on the chess board
      if abs(state[i] - nextX) in (0, nextY -i):
          return True
      return False

#2

def queens(num, state):
    if len(state) == num -1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos

print(list(queens(4, (1, 3, 0))))  # Placing four queens on a 4x4 board

#3

def queens1(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield(pos,)
            else:
                for result in queens1(num, state + (pos,)):
                    yield (pos,) + result

print(list(queens1(3)))
print(list(queens1(4)))
print(len(list(queens1(8))))  # 2147892 but need 92, ???

#4

import random

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))

print(prettyprint(random.choice(list(queens1(8)))))

# 2147892
#X . . . . . . . 
#. . . . . X . . 
#. . . . . . X . 
#. . . . . . . X 
#. . . X . . . . 
#. X . . . . . . 
#. . X . . . . . 
#. . . . . X . . 
