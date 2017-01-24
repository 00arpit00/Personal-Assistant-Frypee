import speech_recognition as sr
import time
import speaking

def record():
    r=sr.Recognizer()

    speaking.speak("Listening...")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            tt=r.recognize_google(audio)
            if tt!="":

                return (tt)
            else:
                record()
        except:
            record()