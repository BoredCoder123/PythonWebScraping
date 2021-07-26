# import requests
# from lxml import html
#
# resp = requests.get("https://en.wikipedia.org/wiki/Main_Page")
# data = html.fromstring(resp.text)
# ans = [data.cssselect("h1"), data.cssselect("h2"), data.cssselect("h3"), data.cssselect("h4"), data.cssselect("h5"), data.cssselect("h6")]
#
# for a in ans:
#     for i in a:
#         print(i.text_content().strip())

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')
