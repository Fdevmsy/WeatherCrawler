# WeatherCrawler
import pyowm

owm = pyowm.OWM('61c7314119e4807ed5343c29a1df8327')  # You MUST provide a valid API key

# You have a pro subscription? Use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Will it be sunny tomorrow at this time in Milan (Italy) ?
# forecast = owm.daily_forecast("Milan,it")
# tomorrow = pyowm.timeutils.tomorrow()
# forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('San Jose,us')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
SpeedDeg = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
humidity = w.get_humidity()              # 87
temperature =  w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print "Weather of San Jose Today"
print "Speed of wind: ", SpeedDeg['speed'] 
print "Deg of wind:", SpeedDeg['deg']
print "Humidity: ", humidity, '%'
print  "Max Temperature: ", temperature['temp_max'] 
print "Current Temperature: ", temperature['temp']
print "Min Temperature: ", temperature['temp_min']


# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
