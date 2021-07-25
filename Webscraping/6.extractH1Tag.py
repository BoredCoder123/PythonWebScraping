import requests
from lxml import html

resp = requests.get("https://example.com/")
data = html.fromstring(resp.text)
ans = data.cssselect("h1")
print(ans[0].text_content())

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.example.com/')
bsh = BeautifulSoup(html.read(), 'html.parser')
print(bsh.h1)
