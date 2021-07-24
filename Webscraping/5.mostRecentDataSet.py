# import urllib.request as req
# from bs4 import BeautifulSoup
#
# data = req.urlopen("https://catalog.data.gov/dataset?q=&sort=metadata_created+desc&as_sfid=AAAAAAUXj6ayp_9LLxrQdW7lrj7ep5rF5YhTEewQ5KFFL5GJ_-iq9nLnI-9C7pPHQIjgTKIRQCGs6gCCGTCqTlCRMLK9Np3OFLamDg31gZqUYFMQqEtsvAJXViK5Nc-othFYh_c%3D&as_fid=6e144caf7a5a323ca13e2b059a1f582fe138ea7e&ext_location=&ext_bbox=&ext_prev_extent=-141.6796875%2C8.754794702435618%2C-59.4140625%2C61.77312286453146")
# soup = BeautifulSoup(data, 'html.parser')
# # print(soup)
# found = soup.find("h3", {"class": "dataset-heading"})
# print(found)
# # found = found.text.replace("\n", "")

from lxml import html
import requests

response = requests.get(
    'https://catalog.data.gov/dataset?q=&sort=metadata_created+desc&as_sfid=AAAAAAUXj6ayp_9LLxrQdW7lrj7ep5rF5YhTEewQ5KFFL5GJ_-iq9nLnI-9C7pPHQIjgTKIRQCGs6gCCGTCqTlCRMLK9Np3OFLamDg31gZqUYFMQqEtsvAJXViK5Nc-othFYh_c%3D&as_fid=6e144caf7a5a323ca13e2b059a1f582fe138ea7e&ext_location=&ext_bbox=&ext_prev_extent=-141.6796875%2C8.754794702435618%2C-59.4140625%2C61.77312286453146')
doc_gov = html.fromstring(response.text)
# print(doc_gov)
link_gov = doc_gov.cssselect('h3.dataset-heading')
# print(type(link_gov[0]))
data = link_gov[0].text_content()
print(data.strip())
