import urllib.request as req
from bs4 import BeautifulSoup

data = req.urlopen("https://catalog.data.gov/dataset")
soup = BeautifulSoup(data, 'html.parser')
found = soup.find("div", {"class": "new-results"})
found = found.text.replace("\n", "")
flag = True
ans = ""
for i, l in enumerate(found, start=0):
    if l == " " and flag is True:
        continue
    else:
        flag = False
        if l == " ":
            break
        else:
            ans = ans + l
print(ans)

# from lxml import html
# import requests
# response = requests.get('http://www.data.gov/')
# doc_gov = html.fromstring(response.text)
# print(doc_gov)
# link_gov = doc_gov.cssselect('small a')[0]
# print("Number of datasets currently listed on data.gov:")
# print(link_gov.text)
