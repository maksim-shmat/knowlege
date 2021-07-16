"""Check palindrome."""

def palindrome(data):
    return data == data[::-1]

print(palindrome("level"))
print(palindrome("madaa"))
