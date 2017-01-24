import urllib2
import Tkinter
import re

import time
import matplotlib
import matplotlib.pyplot as pl


import BeautifulSoup
root=Tkinter.Tk()
root.geometry("400x100+100+100")
label1=Tkinter.Label(root,text="Welcome to Weather Predictor",bg="light blue",font="bold").pack()
Tkinter.Label(root,text="Enter city:").pack()
text=Tkinter.Entry(root,text="")
text.pack()
city=[]


def data():
    city=text.get()
    url="http://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
    try:
        data1=urllib2.urlopen(url).read()
        data2=data1.decode("utf-8")
        #print(data1)
        soup=BeautifulSoup(data2,"html.parser")
        t=soup.find_all("td",class_="num_cell dark temp-color1")
        t+=soup.find_all("td",class_="num_cell dark temp-color2")
        t+=soup.find_all("td",class_="num_cell dark temp-color3")
        t+=soup.find_all("td",class_="num_cell dark temp-color4")
        t+=soup.find_all("td",class_="num_cell dark temp-color5")
        temp_list=[]


        m=re.search('class="temp"', str(t))
        s=m.end()+1
        e=re.search('</span>',str(t))
        l=e.start()
        temp_list.append(int(str(t)[s:l]))
        print(temp_list)

        days=[]
        j=1
        for i in range(1,len(temp_list)+1):
            days.append(j)
            j+=1
        print(days)
        print(temp_list)
        pl.plot(days,temp_list)

        pl.show()

    except:
        label3=Tkinter.Label(root,text="Network Error Or Unknown City")
        label3.pack()
        time.sleep(3)
        root.destroy()



btn=Tkinter.Button(root,text="Show Graph",command=data)
btn.pack()




root.mainloop()


