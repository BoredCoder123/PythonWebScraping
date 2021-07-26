from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re


def listAllUrls(url):
    listOfUrls = []
    try:
        html = urlopen(url)
        bsObj = BeautifulSoup(html, 'html.parser')
        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:
                listOfUrls.append(link.attrs['href'])
    except RuntimeError as r:
        a = 1
    except RuntimeWarning as p:
        a = 1
    except Exception as e:
        a = 1
    return listOfUrls


# print(listAllUrls('#main"'))
