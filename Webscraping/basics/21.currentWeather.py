import requests
from bs4 import BeautifulSoup

site = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Noida&appid=")
jsonData = site.json()
# print(jsonData)
temp = jsonData['main']['temp']
wind = jsonData['wind']['speed']
desc = jsonData['weather'][0]['description']
print(f'{temp} {wind} {desc}')
