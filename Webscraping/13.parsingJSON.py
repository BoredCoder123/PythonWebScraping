from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests

web = requests.get('https://analytics.usa.gov/data/live/realtime.json').json()
print(web['data'][0]['active_visitors'])
