# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# data = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
# parsed = BeautifulSoup(data, 'html.parser')
#
# links = parsed.find_all('a')
#
# for l in links:
#     print(l)
# print(len(links))

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html, 'html.parser')
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
