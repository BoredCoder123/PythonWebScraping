from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('https://en.wikipedia.org/robots.txt')
parsed = BeautifulSoup(data, 'html.parser')

found = parsed.findAll('title')
if len(found) == 0:
    print("No title found")
else:
    print(found)
