"""Reverse game."""

import random
import sys
WIDTH = 8
HEIGHT = 8

def drawBoard(board):
    print('  12345678')
    print(' +--------+')
        for y in range(HEIGHT):
            print('%s|' % (y+1), end='')
            for x in range(WIDTH):
                print(board[x][y], end='')
            print('|%s' % (y+1))

        print(' +--------+')
        print('  12345678')

def getNewBoard():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, title, xstart, ystart):
    if board[xstart][ystart] != ' ' or not is OnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    
    tilesToFlip = []
for xdirection, ydirection in [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1],
        [-1,0], [-1,1]]:
    x, y = xstart, ystart
    x += xdirection
    y += ydirection
    while isOnBoard(x, y) and board[x][y] == otherTile:
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == tile:
            while True:
                x -= xdirection
                y -= ydirection
                if x == xstart and y == ystart:
                    break
                tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

def isOnBoard(x, y):
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

def getBoardWithValidMoves(board, title):
    boardCopy = getBoardCopy(board)
    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    tile = ''
    while not (tile = 'X' or tile == 'O'):
        print('X or O?')
        tile = input().upper()

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'Com'
    else:
        return 'Man'

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile

    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    boardCopy = getNewBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]
    return boardCopy

def isOnCorner(x, y):
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

def getPlayerMove(board, playerTile):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True;
    print("Turn? 'exit' for stop game, or 'tip' for tips.")
        move = input().lower()
        if move == 'exit' or move == 'tip':
            return move

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print("Not true turn. Enter number column(1-8) and number row (1-8).")
            print("For example, value 81 is move up-right corner.")
    return [x, y]

def getComputerMove(board, computerTile):
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)

    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('Your score: %s. Score Com: %s.' % (scores[playerTile], scores[computerTile]))

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print(turn + 'turn first.')

    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board
        
        elif turn == 'Man':
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)

                if move == 'exit':
                    print('Good bye')
                    sys.exit()
                elif move == 'tip':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'Com'
        elif turn == 'Com':
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input('Push Enter for show Com turn.')
                move = getComputerMove(board, computerTile)
                makeMove(board, comuterTile, move[0], move[1])
            turn = 'Man'

print('Hello in the game!')
playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X scores %s points. O scores %s points.' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You win with great of %s points. Congrats' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You loose. Com win you great of % points.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('Draw')
    print('Play more? (yes of no)')
    if not input().lower().startswith('y'):
        break
