import requests as r
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from requests import Timeout, TooManyRedirects, ConnectTimeout
from requests.exceptions import RetryError
from urllib3.exceptions import NewConnectionError

try:
    rh = r.head("https://www.gooasdgle.com/")
    print(f"Able to connect got status code as {rh.status_code}")
except Exception:
    print("Unable to access")

try:
    html = urlopen("https://abcxyz.com")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print(html.read())
