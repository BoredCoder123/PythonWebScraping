import re

link = 'https://www.geeksforgeeks.org/reading-writing-text-files-python/'

if re.match('^www', link) or re.match('^http', link) or re.match('^https', link):
    print(True)
else:
    print(False)