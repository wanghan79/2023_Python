import requests
import sys
from collections.abc import Iterable, Iterator

key = sys.stdin.read().strip('\n')
# print(key)

class WeatherIterator(Iterator):
	def __init__(self, cities, key):
		self.cities = cities
		self.index = 0
		self.key = key
	
	def get_city_Weather(self, city):
		get_info_url = "http://api.openweathermap.org/geo/1.0/direct"
		base_url = "https://api.openweathermap.org/data/2.5/forecast"
		params = {
		"q": city,
		"appid": self.key,
		}
#		print(params)
		info = requests.get(get_info_url, params).json()
#		print(info)
		lat, lon = info[0]['lat'], info[0]['lon']
#		print(lat, lon)
		params = {
			'lat': lat,
			'lon': lon,
			'appid': self.key,
			'exclude': 'current',
			'units': "metric",
		}	
		response = requests.get(base_url, params)
		weather_data = response.json()
#		print(weather_data["list"])
#		print(response)
#		for x in weather_data["list"]:
#			print(x)
		if weather_data["cod"] != 404:
			temperature = weather_data["list"][0]["main"]["temp"]
			return temperature
		else:
			raise Exception("City not found")	

	def __next__(self):
		if self.index >= len(self.cities):
			raise StopIteration
		city = self.cities[self.index]
		self.index += 1
		print("%s当前气温为" % (city), end = " ")
		return self.get_city_Weather(city)
	

class WeatherIterable(Iterable):
	def __init__(self, cities, key):
		self.cities = cities
		self.key = key
	
	def __iter__(self):
		return WeatherIterator(self.cities, self.key)

cities = ["长春市", "北京市","上海市", "秦皇岛市", "南京市", "杭州市", "天津市", "石家庄市", "New York"]

for tp in WeatherIterable(cities, key):
	print("%.2f 摄氏度。" % (tp))
# get_loc_url = "http://api.openweathermap.org/geo/1.0/direct"
# base_url = "https://api.openweathermap.org/data/3.0/onecall"
# key = "532bd74dc64f85b79ba5ceddec9967f6"
# params = {
# "q": "长春市",
# "appid": key,
# }
# response = requests.get(get_loc_url, params)
# response = response.json()
# print(response)	
# print(response[0]["lat"], response[0]["lon"])
# print(key)
