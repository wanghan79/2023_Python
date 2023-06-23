import requests
get_loc_url = "http://api.openweathermap.org/geo/1.0/direct"
base_url = "https://api.openweathermap.org/data/3.0/onecall"
key = "532bd74dc64f85b79ba5ceddec9967f6"
city = "秦皇岛市"
params = {
"q": city,
"appid": key,
}
response = requests.get(get_loc_url, params)
response = response.json()
print(response)	
print(response[0]["lat"], response[0]["lon"])
print(key)
