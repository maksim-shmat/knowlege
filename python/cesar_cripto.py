""" Primitive cripto, shifre of Cesar."""

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('You need to shifre text?')
        mode = input().lower()
        if mode in ['shifre', 's', 'unshifre', 'u']:
            return mode
        else:
            print("Enter 'shifre' or 's' for criptup or 'unshifre' or 'u' fro criptclear.")

def getMessage():
    print('Enter a text:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter a key for the shifre(1-%s)' % (MAX_KEY_SIZE))
        key = int(input())

        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'u':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:  # Symbol not found in SYMBOLS.
            # Just add this simbol without changes
            translated += symbol
        else:
            # Crypt or Uncrypt
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            
            translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Changed text: ')
print(getTranslatedMessage(mode, message, key))
