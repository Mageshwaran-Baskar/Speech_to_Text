import speech_recognition as sr
import pyaudio
r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio=r.listen(source)
    print("time over thanks")

try:
    print("Text : " + r.recognize_google(audio))
except:
    print("Sorry i couldn't hear")