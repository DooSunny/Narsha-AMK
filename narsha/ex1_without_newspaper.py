#pip install beautifulsoup4
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import  urllib.request
import urllib.parse

url = "http://media.daum.net/rss/today/primary/all/rss2.xml"
urls = list()
xml = urllib.request.urlopen(url)
#utf-8로 불러온다
x = xml.read().decode("utf-8")
root = ET.fromstring(x)
titles = list()
for child in root :
    for child2 in root :
        for item in child2.findall('item'):
            titles.append(item.find('title').text)
            urls.append(item.find('link').text)
for url in urls :
    response=urllib.request.urlopen(url)
    soup=BeautifulSoup(response,'html.parser')
    results = soup.select("section > p")
    for result in results :
        print(result.text)