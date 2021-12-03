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

           ===''', '''
           
        +---+
       
       [O   |

       /|\  |

       / \  |

           ===''', '''
        
        +---+

       [O]  |

       /|\  |

       / \  |

           ===''']

words = {'Animals': 'kozel aist akula babuin baran barsuk bobr bik verblud'.split(),
        'Figures': 'square triangle rectangle ring elipse'.split(),
        'Fruits': 'apple orange limon laim pinapple mandarinec banana'.split(),
        'Colors': 'red purple violet tiffany blue black white green'.split()}

def getRandomWord(wordDict):
    """ This func return random str from get dict of list of strings, and key."""
    # In a first random choice get a key from dict.
    wordKey = random.choice(list(wordDict.keys()))

    # In a second random choice get a word from the list of keys in dict.
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)


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
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please, enter LETTER.')
        else:
            return guess

def playAgain():
    # This func return value True if gamer want start new game, elif False.
    print('You want play more? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
difficulty = ''
while difficulty not in 'LMH':
    print('Change level of difficulty: L - Low, M - Mid, H - High')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('Secret word from the set: ' + secretSet)
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
            gameIsDone = True

# Ask player want more?
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretSet = getRandomWord(words)
            else:
                break
"""
Debuging:
    * Need write tests for each functions

"""
