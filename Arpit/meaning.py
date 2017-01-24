import urllib2
import json
import speaking

def mean(title):



    url = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase=' + title + '&pretty=true'
    try:
        data=urllib2.urlopen(url).read()


        #print(data)
        data1=data
        # json representation of url is stored in variable result
        result = json.loads(data1.decode('utf-8'))

        # get the first text in "meaning" in "tuc" from result
        speaking.speak(result["tuc"][0]["meanings"][0]["text"])
    except:
        speaking.speak("Haven't heard of that")
        return
