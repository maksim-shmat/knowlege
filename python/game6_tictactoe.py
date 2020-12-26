""" Tictactoe it is game about crosses and zeros. Artificial inteligence included.
"""

import random

def drawBoard(board):
    """ This function show playfild, squares for checks."""
    # "board" - it is list with 10 strings, for make playing fild(index 0 ignored.
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    """ Player input a letter, return list where letter of player is first 
    element, and leter of com - second.
    """
    letter = ''
    while not(letter =='X' or letter == 'O'):
        print('Your choice X or O?')
        letter = input().upper()

    # The first element of list is letter of player, second - letter of com.
    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']

def whoGoesFirst():
    """ Random choice who's first step."""
    if random.randint(0, 1) == 0:
        return 'Manificent Artificial Inteligence'
    else:
        return 'Leather bastard'

def makeMove(board, letter, move):
    board[move] = letter

def idWinner(bo, le):
    """ True is player win. 'bo' equals board, 'le' equals letter."""
    return((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
           (bo[4] == le and bo[5] == le and bo[6] == le) or # across the center
           (bo[1] == le and bo[2] == le and bo[3] == le) or # across the down
           (bo[7] == le and bo[4] == le and bo[1] == le) or # down from the left side
           (bo[8] == le and bo[5] == le and bo[2] == le) or # down from the center
           (bo[9] == le and bo[6] == le and bo[3] == le) or # down from the right
           (bo[7] == le and bo[5] == le and bo[3] == le) or # down from the diagonal
           (bo[9] == le and bo[5] == le and bo[1] == le)) # down from the diagonal

def getBoardCopy(board):
    """ Make a copy of a play filed."""
    boardCopy = []
    for i in  board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    """ Return True, if get a move to free square."""
    return board[move] == ' '

def getPlayerMove(board):
    """ Access for a player make a move."""
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Your turn... (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    """ Return accessed move with difference list of moves and list of check squares, and None value will be not a moves."""
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if  len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    """ Artificial Inteligent(if) magic in deel."""
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # It is an algorithm for AI 'Tictactoe':
    # first check wariables a win AI in a next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if  isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
        # In a second check win dumb Humans in a next move, and block her.
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, playerLetter, i)
                if isWinner(boardCopy, playerLetter):
                    return i
        # May move to free square.
        move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # May move to the center, if they free.
        if isSpaceFree(board, 5):
            return 5

        # Move for one side
        return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True, if square free. Elif return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Game "TicTacToe"')

while True:
    # Reload playfield
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + 'move first.')
    gameIsPlaying = True

while gameIsPlaying:
    if turn == 'Leather bastart':
        # Humans turn
        drawBoard(theBoard)
        move = getPlayerMove(theBoard)
        makeMove(theBoard, playerLetter, move)

        if isWinner(theBoard, playerLetter):
            drawBoard(theBoard)
            print('Awesome! You win!')
            gameIsPlaying = False
        else:
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print('Draw')
                break
            else:
                turn = 'Manivicien Artificial Inteligence'
    else:
        # Turn com
        move = getComputerMove(theBoard, computerLetter)
        makeMove(theBoard, computerLetter, move)

        if isWinner(theBoard, computerLetter):
            drawBoard(theBoard)
            print('Manivicient Artificial Inteligenc is Win! You loose.')
            gameIsPlaying = False
        else:
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print('Draw')
                break
            else:
                turn = 'Humans'
    print('Play again? (yes or no)')
    if not input().lower().startswith('y'):
        break

