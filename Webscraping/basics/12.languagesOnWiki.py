from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('https://www.wikipedia.org/')
parsed = BeautifulSoup(data, 'html.parser')

found = parsed.findAll('a', {'class': 'link-box'})

for f in found:
    print(f.strong.text, ' ', f.bdi.text)
    print(" ")
