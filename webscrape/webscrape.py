import csv
import os
import subprocess
import requests
from bs4 import BeautifulSoup
url="http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
r= requests.get(url)
soup =BeautifulSoup(r.content)
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
g_write=csv.writer(open("pythonwrite.csv", "w"))
g_write.writerow(["Name","Address", "Zip code", "Phone number"])
#print soup.prettify()
links= soup.find_all("a")
#for link in links:
 #   print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
g_data=soup.find_all("div",{"class":"info"})
for item in g_data:
    print item.contents[0].find_all("a",{"class":"business-name"})[0].text
    try:
         print item.contents[1].find_all("span",{"itemprop":"streetAddress"})[0].text
         a=item.contents[1].find_all("span",{"itemprop":"streetAddress"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span",{"itemprop":"addressLocality"})[0].text.replace(',','')
        b=item.contents[1].find_all("span",{"itemprop":"addressLocality"})[0].text.replace(',','')
    except:
        pass
    try:
        print item.contents[1].find_all("span",{"itemprop":"addressRegion"})[0].text
        c=item.contents[1].find_all("span",{"itemprop":"addressRegion"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span",{"itemprop":"postalCode"})[0].text
        d=item.contents[1].find_all("span",{"itemprop":"postalCode"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("div",{"itemprop":"telephone"})[0].text
        i=item.contents[1].find_all("div",{"itemprop":"telephone"})[0].text
        g_write.writerow([a,b,c,d])
    except:
        pass
    