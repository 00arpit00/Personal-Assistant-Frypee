import json,tkMessageBox
import urllib2
import time
from bs4 import BeautifulSoup,re
import speaking

def fetchData(url):

    URL="http://www.weather-forecast.com/locations/"+url+"/forecasts/latest"
    try:
        res=urllib2.urlopen(URL)
    except:
        speaking.speak("Sorry Haven't listen about it")
        return
    data=res.read()
    soup = BeautifulSoup(data, "html.parser")
    #print(data)
    t = soup.find_all("td", class_="num_cell dark temp-color1")
    t += soup.find_all("td", class_="num_cell dark temp-color2")
    t += soup.find_all("td", class_="num_cell dark temp-color3")
    t += soup.find_all("td", class_="num_cell dark temp-color4")
    t += soup.find_all("td", class_="num_cell dark temp-color5")
    temp_list = []

    m = re.search('class="temp"', str(t))
    s = m.end() + 1
    e = re.search('</span>', str(t))
    l = e.start()
    temp_list.append(int(str(t)[s:l]))
    speaking.speak(str(sum(temp_list)/len(temp_list))+' Degree Celsius')

    #data=json.loads(data)



