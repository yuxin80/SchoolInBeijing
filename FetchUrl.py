# This program fetches the school information from http://bj.lianjia.com/xuequfang/ to build the school data base in JSON format
#

import io
import sys
import urllib.request
import re
from bs4 import *

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

baseurl = "http://bj.lianjia.com/"

xuequfang = "xuequfang"

#get the home page of http://bj.lianjia.com/xuequfang/

html = urllib.request.urlopen(baseurl+xuequfang).read()

soup = BeautifulSoup(html,"html.parser")

allLinks = soup.find_all('a',href=True)

zhongxueLink = ''
ref = re.compile("中学",re.S)
for link in allLinks:
    result = ref.match(str(link))
    print(str(link)+ ' ' + str(result))
    if result:
        zhongxueLink = link["href"]

print(baseurl+zhongxueLink)
#print(soup)
#print(root.prettify().encode("gbk", errors = "ignore").decode("gbk"))
