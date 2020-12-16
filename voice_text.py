""" Change text to voice."""

# pip3 install gtts
# pip3 install playsound

from gtts import gTTS
from playsound import playsound

audio = 'seech.mp3'
language = 'ru'
sp = gTTS(text = "Input your text that neee to converte to audio file soska",
        lang = language, slow = False)
sp.save(audio)
playsound(audio)
