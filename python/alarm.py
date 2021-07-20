""" Make alarm with time module from Python."""

import time
import pygame.mixer.music

def myAlarm():
    try:
        myTime = list(map(int, input("Input time in hours, minutes and secunds\n").split()))
        if len(myTime) == 3:
            total_seconds = myTime[0]*60*60+myTime[1]*60 + myTime[2]
            time.sleep(total_seconds)
            frequency = 2500  # 2500 Hz
            duration = 1000   # long 1000 ms == 1 sec
            winsound.Beep(frequency, duration)
        else:
            print("Please, input time in true format, that it write, bitch\n")
            myAlarm()
    except Exception as e:
        print("It is exception, man\n",e,"Please, input true data, dumbitch")
        myAlarm()
myAlarm()
