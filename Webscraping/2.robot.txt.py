import urllib.request
import requests
from bs4 import BeautifulSoup

robot = urllib.request.urlopen("https://en.wikipedia.org/robots.txt")
soup = BeautifulSoup((robot.read()), 'html.parser')
print(soup.title)
print(soup)
# print("nextone")
# response = requests.get("https://en.wikipedia.org/robots.txt")
# print(response.text)
