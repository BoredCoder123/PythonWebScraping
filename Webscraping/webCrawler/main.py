from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import listAllUrls
import os.path
import re


def main():
    basicUrl = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    maxCnt = 10000
    cnt = 2

    DIR = './crawled'
    length = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) + 1

    file1 = open(f'./crawled/{length}.txt', 'w')
    file1.write(f'b\'{basicUrl}\'\n')
    myDict = {basicUrl: 0}

    while cnt <= maxCnt:
        for item in list(myDict):
            listOfUrls = listAllUrls.listAllUrls(item)
            for link in listOfUrls:
                if (re.match('^www', str(link)) or re.match('^http', str(link)) or re.match('^https',
                                                                                            str(link))) and link not in list(
                        myDict):
                    cnt = cnt + 1
                    myDict[link] = 0
                    link = link.encode('utf-8')
                    file1.write(f'{link}\n')
                if cnt > maxCnt:
                    break
            if cnt > maxCnt:
                break

    # link = link.attrs['href']
    # if re.match('^www', link) or re.match('^http', link) or re.match('^https', link):
    # file1.write(f'{l}\n')

    file1.close()

    file1 = open(f'./crawled/{length}.txt', 'r')
    file2 = open(f'./crawled/{length+1}.txt', 'w')

    for aline in file1:
        temp = aline[2: -2]
        file2.write(f'{temp}\n')

    file1.close()
    file2.close()


main()
