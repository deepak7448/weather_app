# import pygeoip
# gi = pygeoip.GeoIP('GeoIP.dat')
# gi.country_name_by_addr('64.233.161.99')
# print(gi)

import requests
import json
ip=requests.get("https://get.geojs.io//v1/ip/geo.json").json()
ct=ip['city']
weather=requests.get("http://api.weatherapi.com/v1/forecast.json?key=apikey&q=delhi&days=1&aqi=no&alerts=no").json()
wt=weather['location']
wet=[]
Weather={
    'forcast':weather['forecast']['forecastday'][0]['date'],
    'max':weather['forecast']['forecastday'][0]['day']['maxtemp_c'],
    'min':weather['forecast']['forecastday'][0]['day']['mintemp_c'],
    'sunrise':weather['forecast']['forecastday'][0]['astro']['sunrise'],
    'sunset':weather['forecast']['forecastday'][0]['astro']['sunset'],
    'hour':weather['forecast']['forecastday'][0]['hour'][8]['time'],
}
wet.append(Weather)
# print(wet)
for i in wet:
    # for j in i["hour"][1:24:2]:
    #     print("Time",j['time'])
    #     print("temp_c",j['temp_c'])
    #     print("condition",j['condition']['text'])
    #     print("wind_mph",j['wind_mph'])
    #     print("wind_degree",j['wind_degree'])
    #     print("wind_dir",j['wind_dir'])
    #     print("cloud",j['cloud'])
    #     print("vis_miles",j['vis_miles'])
    #     print("gust_mph",j['gust_mph'])
    print(i)