""" Mr.Babbage count his units in piramid
    *
   * *  +1
  * * *  +1
 * * * *  +1
 """
MarbRows = input("Enter how many rows in piramid: ")
MarbRows = int(MarbRows)
MarbNum = int((MarbRows) * (MarbRows + 1) / 2)
print("Count units equals: " + str(MarbNum))
