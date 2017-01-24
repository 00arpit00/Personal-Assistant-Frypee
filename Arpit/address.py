import urllib2
import json
import speaking
def locate():
    url='http://freegeoip.net/json'
    data=urllib2.urlopen(url)
    js=json.loads(data.read())
    lat=js['latitude']
    lon=js['longitude']
    #print(lat,lon)
    locurl='http://maps.googleapis.com/maps/api/geocode/json?latlng='+str(lat)+','+str(lon)+'&sensor=false'
    data1=urllib2.urlopen(locurl).read()
    data2=json.loads(data1)
    x=data2['results'][0]['address_components']
    speaking.speak(x[4]['long_name'])
def locate2(location):
    url = 'http://freegeoip.net/json'
    data = urllib2.urlopen(url)
    js = json.loads(data.read())
    lat = js['latitude']
    lon = js['longitude']
    # print(lat,lon)
    locurl = 'http://maps.googleapis.com/maps/api/geocode/json?address='+location+'&sensor=false'
    data1 = urllib2.urlopen(locurl).read()
    data2 = json.loads(data1)
    #print(data1)
    x=data2['results'][0]['formatted_address']
    speaking.speak(x)
