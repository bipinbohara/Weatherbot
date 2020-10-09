import json
import logging
from Packages import *
#import requests
import urllib3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler1(event, context, city_name):
    logger.debug(event)
    http = urllib3.PoolManager()
    
    api_key = '9fdb700b5a2efd806c8ffd6f356e559f'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    
    #city_name = "London"
    
    finalurl = base_url + 'appid=' + api_key + '&q=' + city_name
    
    #response = requests.get(finalurl)
    r = http.request('GET', finalurl)
    x = json.loads(r.data.decode('utf-8'))
    y = x['main']
    current_temperature = y['temp']
    current_pressure = y['pressure']
    current_humidiy = y['humidity']
    z = x['weather']
    weather_description = z[0]['description']
    
    content = "Temperature (in Farenheit) = " + str("%.2f" % current_temperature) + "\nAtmospheric pressure (in hPa) = " + str(current_pressure) + "\nHumidity (in percentage) = " + str(current_humidiy) + "\nDescription = " + str(weather_description)
    
    #content = "You are trapped in test."
    return (content)
