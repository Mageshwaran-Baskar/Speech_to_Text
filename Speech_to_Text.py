from speech_recognition import Microphone as Mic
from speech_recognition import Recognizer as r
import pyaudio

with Mic():
    print("say something")
    audio=r.listen(Mic)
    print("time over thanks")

try:
    print("Text : " + r.recognize_google(audio))
except:
    print("Sorry i couldn't hear you")
