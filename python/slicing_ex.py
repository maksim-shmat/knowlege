"""Examples for the slicing."""

#1 Split up a URL of the form http://www.something.com

url = input('Please enter the URL:')
domain = url[11:-4]
print("Domain name:" + domain)

#2 letters = 'abcdefghijklmnopqrstuvwxyz'

letters[:]  # whole the string

letters[20]  # from 20 to end string
'uvwxyz'

letters[10:15]  # from 10 to 15
'mno'

letters[-3:]  # last three letters
'xyz'

letters[18:-3]  # from 18 to -3
'stuvw'

letters[::7]  # step 7
'ahov'

letters[4:20:3]  # each third letter from 4 to 20, step 3{
'ehknqt'

letters[19::4]  # each fourth letter from 19 to end, step 4
'tx'

letters[:21:5]  #  from start to 21, step 5
'afkpu'

letters[-1::-1]  # from end to start
letters[::-1]  # same
'zyxwvutsrqponmlkjihgfedcba'

