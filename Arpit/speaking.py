import pyttsx
def speak(audioString):
    print(audioString)
    engine= pyttsx.init()
    engine.say(audioString)

    engine.runAndWait()

