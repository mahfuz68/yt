import re
import urllib.request

import requests

link = input('enter your fb video url:>')
html = requests.get(link)

try:
    url= re.search('hd_src"(.+?)"',html.text)[1]
    print('found the hd quality!')

except:
    url= re.search('sd_src"(.+?)"',html.text)[1]
    print('found the sd quality!')

print('download the video...')
urllib.request.urlretrieve(url, "Video.mp4")
