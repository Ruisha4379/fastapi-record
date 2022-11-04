"""
date: 2022-11-04
Test openweather geocoding API 
"""
import requests
#from tkinter import * # for grafical interface
import math

api_key = "xx"

def get_location(zip_code,country_code): #zip_code,country_code
    url= f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
    response = requests.get(url).json()
    #zip = response['zip']
    lat = response['lat']
    lon = response['lon']
    print(response)
    return {
        'lattitude':lat,
        'longtitude':lon
    }
loc = get_location("554533", "SG")
print(loc)
