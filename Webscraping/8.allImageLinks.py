from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen("https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)")
bs = BeautifulSoup(data, 'html.parser')

links = bs.find_all('img')
for l in links:
    print(l['src'])
