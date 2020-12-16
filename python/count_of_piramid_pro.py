""" Mr.Babbage don't stop and count his balls, and now he tell us 

how many you have rows with your count balls, ant how many remaining in trash.

    *
   * *  +1
  * * *  +1    *
 * * * *  +1  ***
 """
import math

MarbNum = input("Enter how many balls you have: ")
MarbNum = int(MarbNum)

firstguess = int(math.sqrt(MarbNum*2)) # if sqrt have a not float integer

if (firstguess * (firstguess + 1) > MarbNum*2):
    rectNum = firstguess - 1
else:
    correctNum = firstguess    # if sqrt float that error, sorry.

MarbRem = int(MarbNum - (correctNum*(correctNum+1)/2))
if MarbRem == 0:
    MarbRem = "no"
if MarbRem == 1:
    marbleword = "marble"
else:
    marbleword = "marbles"
print("You can have: ", correctNum, "rows, with", MarbRem, marbleword, "remaining.")
