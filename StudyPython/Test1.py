# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import io
import sys
import urllib.request
from bs4 import *

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

#print(html)

soup = BeautifulSoup(html,"html.parser")

# Retrieve all of the anchor tags
tags = soup.find_all('a',href=True)
for tag in tags:
    # Look at the parts of a tag
    print ('TAG:',tag)
    #print ('Contents:',tag.contents[0])
    print ('Attrs:',tag['href'])

#print(soup.prettify())
