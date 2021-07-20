""" Play music, but I don't have any tracks."""

from pygame import mixer

mixer.init()  # start mixer
# if error start from terminal or change conf

mixer.music.load("song.mp3")  # load music
# if error change data format

mixer.music.set_volume(0.7)  # set volume
mixer.music.play()  # play

while True:
    print("Press 'p' for pause, and "r" for restart")
    print("Press 'e' for exit")
    query = input(">>>")

    if query == 'p':
        mixer.music.pause()  # pause
    elif query == 'r':
        mixer.music.unpause()  # restart
    elif query == 'e':
        mixer.music.stop() # stop and exit
        break
