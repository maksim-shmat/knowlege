""" This game from dumb field pinokio."""

import random
HANGMAN_PICS = ['''
        +---+
            
            |
            
            |
            
            |
           
           ===''', '''

        +---+
            
            |
             
             |

             |
             
           ===''', '''

        +---+
            
        O   |

        |   |

            |

           ===''', '''

        +---+
        
        O   |
       
       /|   |

            |

           ===''', '''

        +---+

        O   |
       
       /|\  |

            |
           
           ===''', '''

        +---+

        O   |

       /|\  |

       /    |

           ===''', '''

        +---+

        O   |
       
       /|\  |

       / \  |

           ===''']
words = 'kozel aist akula babuin baran barsuk bobr bik verblud'.split()

def getRandomWord(wordList):
    """ This func return random str from get list."""
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # change _ fot letter
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show secret word with _ between letters
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Return letter if gamer write. And check that letter is one.
    while True:
        print('Write letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please, input one letter.')
        elif guess in alreadyGuessed:
            print('You already write this letter, olegafriend. Write another!')
        elif guess not in 'abcdefghijklmnorstuvwxyz':
            print('Please, enter LETTER.')
        else:
            return guess

def playAgain():
    # This func return value True if gamer want start new game, elif False.
    print('You want play more? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Accessed for player to write a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check that player win
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('YES! The secret word - "' + secretWord + '"! Your win!')
            gameIsDone = True
        else:
            missedLetters = missedLetters + guess
            # Check go up player's limit and lose
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetter, secretWord)
print('This is the end.\n Loose leters: '+str(len(missedLetters))+'and check:'+str(len(correctLetters))+'.General Word is"'+secretWord+'".')
igameIsDone = True

# Ask player want more?
if gameIsDone:
    if playAgain():
        missedLetters = ''
        correctLetters = ''
        gameIsDone = False
        secretWord = getRandomWord(words)
    #else:
    #    break
