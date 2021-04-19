from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
import requests
import os
import json
from datetime import datetime, date, time
from requests.exceptions import ConnectionError


# def daily(request):
#     search = request.GET['q']
#     weather_url = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=c24d3c9a5d00456d8ff70958210604&q={search}&days=1&aqi=no&alerts=no").json()
#     daily_weather=[]
#     x=datetime.now()
#     now= x.time()
#     for current in weather_url['forecast']['forecastday'][::1]:
#         hr = current['hour']
#         for daily in hr:
#             time = daily['time']
#             times = datetime.strptime(time,'%Y-%m-%d %H:%M').time()
#             dates = datetime.strptime(time,'%Y-%m-%d %H:%M').date()
#             if now < times:
#                 curt_time = times.strftime('%I %p')
#                 curt_date = dates.strftime('%m-%d')
#                 coll = times.strftime('%I')
#                 weather={
#                     "coll":coll,
#                     "time":curt_time,
#                     "date":curt_date,
#                     "temp_c":daily['temp_c'],
#                     "condition":daily['condition']['text'],
#                     "icon":daily['condition']['icon'],
#                     "wind":daily['wind_kph'],
#                     "wind_chill":daily['windchill_c'],
#                     "pressure_in":daily["pressure_in"],
#                     "precip_mm":daily["precip_mm"],
#                     "humidity":daily["humidity"],
#                     "cloud":daily["cloud"],
#                     "heatindex":daily["heatindex_c"],
#                     "dewpoint":daily["dewpoint_c"],
#                     "chance_of_rain":daily["will_it_rain"],
#                     "visibility":daily["vis_km"],
#                     "uv":daily["uv"]}
#                 daily_weather.append(weather)
#     return daily_weather

# def forecast(request):
#     search = request.GET['q']
#     weather_url = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=c24d3c9a5d00456d8ff70958210604&q={search}&days=3&aqi=no&alerts=no").json()
#     fore=[]
#     for j in weather_url['forecast']['forecastday'][::1]:
#         date =  j['date']
#         dates = datetime.strptime(date,'%Y-%m-%d').date()
#         curt_date = dates.strftime('%m-%d')
#         coll = dates.strftime('%d')
#         forecast={
#             "coll":coll,
#             "date" :curt_date,
#             "max_temp" : j["day"]["maxtemp_c"],
#             "min_temp" : j["day"]["mintemp_c"],
#             "avgtemp_c" : j["day"]["avgtemp_c"],
#             "wind_kph" :  j["day"]["maxwind_kph"],
#             "precip_mm" : j["day"]["totalprecip_mm"],
#             "vis_km" : j["day"]["avgvis_km"],
#             "humidity" : j["day"]["avghumidity"],
#             "chance_of_rain" : j["day"]["daily_chance_of_rain"],
#             "condition" : j["day"]['condition']['text'],
#             "icon" : j["day"]['condition']['icon'],
#             "uv" : j["day"]['uv'],
#             "sunrise" : j["astro"]["sunrise"],
#             "sunset" : j["astro"]["sunset"],
#             "moon_phase" : j["astro"]["moon_phase"]}
#         fore.append(forecast)
#     return fore

def location_weather(request):
    while True:
        try:
            ip=requests.get("https://get.geojs.io/v1/ip/geo.json").json()
            ct=ip['city']
            weather_url = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=c24d3c9a5d00456d8ff70958210604&q={ct}&days=3&aqi=no&alerts=no").json()
            daily=[]
            fore = []
            x=datetime.now()
            current_date = x.date()
            current_time = x.time()
            coll = current_date.strftime('%Y-%m-%d')
            #print(coll)
            for j in weather_url['forecast']['forecastday'][::1]:
                date = j['date']
                hour = j['hour']
                if coll == date:
                    for i in hour:
                        time = i['time']
                        times = datetime.strptime(time,'%Y-%m-%d %H:%M').time()
                        dates = datetime.strptime(time,'%Y-%m-%d %H:%M').date()
                        if current_time < times:
                            curt_time = times.strftime('%I %p')
                            curt_date = dates.strftime('%m/%d')
                            coll = times.strftime('%I%p')
                            weather={
                                "coll":coll,
                                "time":curt_time,
                                "date":curt_date,
                                "temp":i['temp_c'],
                                "condition":i['condition']['text'],
                                "icon":i['condition']['icon'],
                                "wind":i['wind_kph'],
                                "wind_chill":i['windchill_c'],
                                "pressure_in":i["pressure_in"],
                                "precip_mm":i["precip_mm"],
                                "humidity":i["humidity"],
                                "cloud":i["cloud"],
                                "heatindex":i["heatindex_c"],
                                "dewpoint":i["dewpoint_c"],
                                "chance_of_rain":i["will_it_rain"],
                                "visibility":i["vis_km"],
                                "uv":i["uv"]}
                            daily.append(weather)
                date =  j['date']
                dates = datetime.strptime(date,'%Y-%m-%d').date()
                curt_date = dates.strftime('%m-%d')
                coll = dates.strftime('%d')
                forecast={
                    "coll":coll,
                    "date" :curt_date,
                    "max_temp" : j["day"]["maxtemp_c"],
                    "min_temp" : j["day"]["mintemp_c"],
                    "avgtemp_c" : j["day"]["avgtemp_c"],
                    "wind_kph" :  j["day"]["maxwind_kph"],
                    "precip_mm" : j["day"]["totalprecip_mm"],
                    "vis_km" : j["day"]["avgvis_km"],
                    "humidity" : j["day"]["avghumidity"],
                    "chance_of_rain" : j["day"]["daily_chance_of_rain"],
                    "condition" : j["day"]['condition']['text'],
                    "icon" : j["day"]['condition']['icon'],
                    "uv" : j["day"]['uv'],
                    "sunrise" : j["astro"]["sunrise"],
                    "sunset" : j["astro"]["sunset"],
                    "moon_phase" : j["astro"]["moon_phase"]}
                fore.append(forecast)
        except ConnectionError:
            return render(request,'error.html')
        except KeyError:
            pass
        content={
                'weather_url':weather_url,
                'daily_weather':daily,
                'forecast_weather':fore
            }
        return render(request,'loc_weather.html',content)

def search(request):
    try:
        search = request.GET['q']
        print(search)
        weather = f"http://api.weatherapi.com/v1/forecast.json?key=c24d3c9a5d00456d8ff70958210604&q={search}&days=3&aqi=no&alerts=no"
        weather_url = requests.get(weather).json()
        daily=[]
        fore = []
        x=datetime.now()
        current_date = x.date()
        current_time = x.time()
        coll = current_date.strftime('%Y-%m-%d')
            #print(coll)
        for j in weather_url['forecast']['forecastday'][::1]:
            date = j['date']
            hour = j['hour']
            if coll == date:
                for i in hour:
                    time = i['time']
                    times = datetime.strptime(time,'%Y-%m-%d %H:%M').time()
                    dates = datetime.strptime(time,'%Y-%m-%d %H:%M').date()
                    if current_time < times:
                        curt_time = times.strftime('%I %p')
                        curt_date = dates.strftime('%m/%d')
                        coll = times.strftime('%I')
                        weather={
                            "time":curt_time,
                            "date":curt_date,
                            "temp":i['temp_c'],
                            "condition":i['condition']['text'],
                            "icon":i['condition']['icon'],
                            "wind":i['wind_kph'],
                            "wind_chill":i['windchill_c'],
                            "pressure_mb":i["pressure_mb"],
                            "precip_mm":i["precip_mm"],
                            "humidity":i["humidity"],
                            "cloud":i["cloud"],
                            "heatindex":i["heatindex_c"],
                            "dewpoint":i["dewpoint_c"],
                            "chance_of_rain":i["will_it_rain"],
                            "visibility":i["vis_km"],
                            "uv":i["uv"]}
                        daily.append(weather)
            date =  j['date']
            dates = datetime.strptime(date,'%Y-%m-%d').date()
            curt_date = dates.strftime('%m-%d')
            coll = dates.strftime('%d')
            forecast={
                "coll":coll,
                "date" :curt_date,
                "max_temp" : j["day"]["maxtemp_c"],
                "min_temp" : j["day"]["mintemp_c"],
                "avgtemp_c" : j["day"]["avgtemp_c"],
                "wind_kph" :  j["day"]["maxwind_kph"],
                "precip_mm" : j["day"]["totalprecip_mm"],
                "vis_km" : j["day"]["avgvis_km"],
                "humidity" : j["day"]["avghumidity"],
                "chance_of_rain" : j["day"]["daily_chance_of_rain"],
                "condition" : j["day"]['condition']['text'],
                "icon" : j["day"]['condition']['icon'],
                "uv" : j["day"]['uv'],
                "sunrise" : j["astro"]["sunrise"],
                "sunset" : j["astro"]["sunset"],
                "moon_phase" : j["astro"]["moon_phase"]}
            fore.append(forecast)
    except ConnectionError:
        return render(request,'error.html')
    except KeyError:
        pass
    content={
        'weather_url':weather_url,
        'search':search,
        'daily_weather':daily,
        'forecast_weather':fore
    }
    return render(request,'loc_weather.html',content)