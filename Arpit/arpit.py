from time import ctime
import openapp
import control
import forecast
import address

import microphone
import speaking,sys
def recordAudio():
    while True:
        global t,x
        if t==1:
            break
        if x==1:
           control.bot()
        data=microphone.record()
        t=decoder(data)


    sys.exit(0)



def speak(audioString):
    speaking.speak(audioString)





def decoder(data):
    if data!=None:
        print data
        if "how are you" in data:
            speak("I am fine")
            recordAudio()

        if 'what are you' in data:
            speak("I am a virtual assistant with unique abilities I can search for words for you     Measuring temperature of a city locating your position are some of my abilities.")
            recordAudio()

        if "what time is it" in data:
            speak(ctime())
            recordAudio()

        if "where is" in data:
            data= data.split(" ")
            location = " ".join(data[2:])
            address.locate2(location)
            (location)
            recordAudio()

        if 'my location' in data:
            address.locate()
            recordAudio()

        if "temperature" in data or 'Temperature' in data:
            forecast.fetchData(data.split(" ")[-1])
            recordAudio()
        if "Meaning" in data or 'meaning' in data:
            data=data.split(" ")
            import meaning

            meaning.mean(" ".join(data[2:]))
            recordAudio()

        if "exit" in data:
            speak("GoodBye")

            return 1
        return 0

    else:
        speak("Sorry I didn't hear you")
        recordAudio()



# initialization
#if __name__=="__main__":
t=0
x=0
speak("Hi Arpit, what can I do for you?")
recordAudio()
