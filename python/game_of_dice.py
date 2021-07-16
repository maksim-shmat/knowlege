""" one and one it is eyes of Death, right."""

from random import randint

def roll_die(eyes,amount):
    '''
    function that rolls die based on die data.
    returns die_roll list
    '''

    die_roll = [randint(1,eyes) for die in range(0,amount)]
    return die_roll


def keep_die(die_list,source_roll):
    '''
    function that collects the die a player wants to keep.
    returns split_to_int list with die
    '''
    split_die_list = die_list.split(',')
    split_to_ints = [int(item) for item in split_die_list]
    return split_to_ints


def main():
    eyes_on_dice = 6
    number_of_die = 5
    number_of_rolls = 3

    keep_die_list = []

    counter = 1
    while counter<number_of_rolls:
        rolled_die = roll_die(eyes_on_dice,number_of_die)
        print(f'\nrolled: {rolled_die}')

        keep = input('To keep die, type number and commas to separate them(ex. 4,5,5)\nPress enter to not keep any: ')
        if keep == '':
            conter+=1

        else:
            add_die_to_keep = keep_die(keep,rolled_die)
            print(f'keeping: {add_die_to_keep}')

            # append selection to keep list
            for item in add_die_to_keep:
                keep_die_list.append(item)
            number_of_die = number_of_die - len(add_die_to_keep)
            counter=+1

    # the last throw is force kept
    for item in rolled_die:
        keep_die_list.append(item)

    print(f'Your die: {keep_die_list}')

main()
