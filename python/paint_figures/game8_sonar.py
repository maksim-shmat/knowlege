""" Treasures hunt with sonar in sea."""

import random
import sys
import math

def getNewBoard():
    """ Make a structure of data in playfield size 60x15."""
    board = []
    for x in range(60):  # Head list with 60 lists
        board.append([])

    for y in range(15):  # Each list in head list have 15 onecharacter string.
        if random.randint(0, 1) == 0:
            board[x].append('~')
        else:
            board[x].append('`')
    return board

def drawBoard(board):
    """ Draw playfield."""
    tensDigitsLine = ' '  # Make place for digits to down in left side.
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # Return digits in upside of field.
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()

    # Return each of 15 rows.
    for row in range(15):

# Add space to digits.
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        # Make a string for this row on the playfield.
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

    print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    # Return digits in down side of playfield.
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    # Make a list of structure of data of chest(two elements list of coord x,y
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
    if newChest not in chests:  # Make sure that chest is not
        chests.append(newChest)
    return chests

def isOnBoard(x, y):
# Return Truek, if coord on the field, elif False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    """ Change data structure of field, with simbol hidrolocator. Del chests
    with treasures from the list of chests, how you check their. Return False
    if it not accessed move. Elif return string with results of one move.
    """
    smallesDistance = 100  # All chests less than 100 pts.
    for cx, cy in chests:
        distance = mathsqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

    if distance < smallestDistance:
        smallestDistance = distance
        smallestDistance = round(smallestDistance)
        
        if smallestDistance == 0:
# Coord xy on the chest.
            chests.remove([x, y])
            return 'You have a chest of treasures!'
        else:
            if smallestDistance < 10:
                board[x][y] = str(smallestDistance)
                return 'Chest in th %s from hydrolocator.' % (smallestDistance)
            else:
                board[x][y] = 'X'
            return 'Hydrolocator nothing.'

def enterPlayerMove(previousMoves):
    # Player make a move. Return coord x,y.
    print('Where is check from hydrolockator? (coord: 0-59 0-14)(or ener "exit")')
    while True:
        move = input()
        if move.lower() == "exit":
            print('Thank you for game!')
            sys.exit()

        move = move.split()
    if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
        if [int(move[0]), int(move[1])] in previousMoves:
            print('Thire`s we have already.')
    continue
    return [int(move[0]), int(move[1])]
    print('Enter an interger from 9 to 59, after space, ant then integer from 0 to 14.')

def showInstructions():
    print(""" Instructions:
    You is a captain of ship, which move to the treasures. You target with
    hydrolocators make a fortune. But hyfrolocators show only length not
    curse. Enter coord that move hydrolocator. On the map will be show
    integer that value how far chest. X - it is chest there. C - chest.
    Enter for play. """)
    input()

print("Go!")
print()
print('Show instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    # Game settings
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
# Show sonars and chests
        print('All sonars is: %s. All chsts is: %s.'%(sonarDevices, len(theChests)))
    x, y = enterPlayerMove(previousMoves)
previousMoves.append([x, y]) # checks all moves for visual sonars.

moveResult = makeMove(theBoard, theChests, x, y)
if moveResult == False:
    continue
else:
    if moveResult == 'You check chest!':
        # Reload sonars
        for x, y in previousMoves:
            makeMove(theBoard, theChests, x, y)
    drawBoard(theBoard)
    print(moveResult)

if len(theChests) == 0:
    print('You checked all chests!')
break
sonarDevices -= 1
if sonarDevices == 0:
    print('All sonars on the deep! That`s all, this is the end')
    print('Go out looser, game over.')
    print('You not checked chsts in these:')
    for x, y in theChests:
        print(' %s, %s' % (x, y))

    print('Have you more a chance? (yes or no)')
    if not input().lower().startswith('y'):
        sys.exit()
