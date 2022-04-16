"""Detecting Palindromes e.g. 'IPrefer Pi'."""

def is_palindrome(text):
    n = len(text)
    for i in range(len(text) // 2):
        if text[i] != text[n-i-1]:
            return False
    return True

#1 new

def reverse(text):
    return text[::-1]  # from start to end in backward
def is_palindrome(text):
    return text == reverse(text)

something = input('Enter text: ')
if (is_palindrome(something)):
    print('Yes, it is palindrome')
else:
    print('Nope, it is not a palindrome')
