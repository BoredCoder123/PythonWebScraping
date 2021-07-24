# import geopandas
# import geopy
# from geopy import Nominatim
#
# locator = Nominatim(user_agent="myGeocoder")
# location = locator.geocode("India Gate, India")
# print(f'{location.latitude} {location.longitude}')

import requests
geo_url = 'http://maps.googleapis.com/maps/api/geocode/json'
my_address = {'address': 'India Gate, Rajpath, India Gate, New Delhi, Delhi 110001, India',
             'language': 'en'}
response = requests.get(geo_url, params = my_address)
results = response.json()['results']
my_geo = results[0]['geometry']['location']
print("Longitude:",my_geo['lng'],"\n","Latitude:",my_geo['lat'])
