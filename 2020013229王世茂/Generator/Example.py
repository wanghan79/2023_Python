import requests
import sys
from collections.abc import Iterable, Iterator

if len(sys.argv) != 1:
	print(sys.argv[1])

class WeatherIterator(Iterator):
	def __init__(self, cities):
		self.cities = cities
		self.index = 0
		self.apikey = "532bd74dc64f85b79ba5ceddec9967f6"
	
	def get_city_Weather(self, city, api_key):
		get_loc_url = "http://api.openweathermap.org/geo/1.0/direct?q={city}"
		base_url = "https://api.openweathermap.org/data/3.0/onecall"
		
		params = {
			'lat': 0,
			'lon': 0,
			'appid': api_key,
			'units': "metric",
		}	
		response = requests.get(base_url, params)
		weather_data = response.json()
		if weather_data["cod"] != 404:
			temperature = weather_data["current"]["temp"]
			return temperature
		else:
			raise Exception("City not found")	

	def __next__(self):
		if self.index >= len(self.cities):
			raise StopIteration
		city = self.cities[self.index]
		self.index += 1
		return self.getWeather(city)
	

class WeatherIterable(Iterable):
	def __init__(self, cities):
		self.cities = cities
	
	def __iter__(self):
		return WeatherIterator(cities)

cities = ["长春", "北京","上海"]

# for tp in WeatherIterable(cities):
#	print(tp)

get_loc_url = "http://api.openweathermap.org/geo/1.0/direct"
base_url = "https://api.openweathermap.org/data/3.0/onecall"
key = "532bd74dc64f85b79ba5ceddec9967f6"
params = {
"q": "伦敦",
"appid": key,
}
response = requests.get(get_loc_url, params)
response = response.json()
print(response)	
print(key)
