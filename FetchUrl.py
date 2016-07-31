# This program fetches the school information from http://bj.lianjia.com/xuequfang/ to build the school data base in JSON format
#

import io
import sys
import urllib.request
import re
from bs4 import *
import imp

imp.reload(sys)

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

baseurl = "http://bj.lianjia.com/"

xuequfang = "xuequfang"

#get the home page of http://bj.lianjia.com/xuequfang/

html = urllib.request.urlopen(baseurl+xuequfang).read()

htmlStr = str(html,'utf8')

soup = BeautifulSoup(htmlStr,"html.parser")

#find the link for middle school entry
allLinks = soup.find_all('a',href=True)

zhongxueLink = ''
restr = "中学\d+所"
ref = re.compile(restr)
for link in allLinks:
     result = ref.search(str(link))
    #  print(result)
    #  print(str(link)+': '+ str(result))
     if result:
         zhongxueLink = link["href"]

print(baseurl+zhongxueLink)

#get the data for all schools
i=1

lists = soup.find_all('ul')

for l in lists:
    # print(l.prettify())
    schools = l.children
    # print(schools)
    # print("-----------------------------")
    for c in schools:
        print(c)
