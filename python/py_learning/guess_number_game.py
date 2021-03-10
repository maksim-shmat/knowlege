""" The game ends when the player manages to guess the number."""

from random import randint

def computer_number(min_num,max_num):
    '''
    function that generates a random number based on the range passed as args.
    returns random int
    '''
    return randint(min_num,max_num)

def player_guess(min_num,max_num):
    '''
    function that asks the player for a number.
    returns random int
    '''
    user_input = int(input(f'guess a nuber between {min_num} and {max_num}: '))
    return user_input

def play():
    # define high and low guessing range
    low = 0
    high = 10

    # get input from computer and player
    computer_choice = computer_number(low,high)
    player_choice = player_guess(low,high)

    # loop until player guesses the number
    while player_choice != computer_choice:
        if player_choice>computer_choice:
            player_choice = int(input('Number is too high, try again: '))
        elif player_choice<computer_choice:
            player_choice = int(input('Number is too low, try again: '))

    print(f'Congratulation! You managed to guess the number {computer_choice}')
play()
