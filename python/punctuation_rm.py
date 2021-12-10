"""Remove Punctuation from a string."""

punctuations = '''"'`~!@#$%^&*()-_=+{}[]\|:;,.<>?'''
orgStr = "Hi!!, Welcome, Tutti_pathway?"
newStr = ""
for char in orgStr:
    if char not in punctuations:
        newStr = newStr + char

print("\nThe Original String Before Removing Punctuations")
print(orgStr)
print("\nThe Final String After Removing Punctuations")
print(newStr)
