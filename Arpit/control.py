
import urllib
import speaking
import microphone
def bot():
    speaking.speak("What do you want to search")
    data=microphone.record()
    data=urllib.quote(data)
    print(data)