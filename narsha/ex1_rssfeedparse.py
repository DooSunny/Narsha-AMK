import xml.etree.ElementTree as ET
import urllib.request
from urllib import parse
#-*- coding:utf-8 -*-

s = input("검색어를 입력하세요 : ")
search = parse.quote(s)
#print(search)

#쿼리를 받아올 주소
#url = "http://newssearch.naver.com/search.naver?where=rss&query="+search+"&field=0&nx_search_query=&nx_and_query=&nx_sub_query=&nx_search_hlquery=&is_dts=0"
#print(url)
#url = "https://search.naver.com/search.naver?where=news&query=%EA%B0%80%EC%A7%9C%20%EB%89%B4%EC%8A%A4&sm=tab_pge&sort=0&photo=0=&field=0&pd=0&ds=&de=&refresh=-1&docid="
url = "https://media.daum.net/syndication/today_sisa.rss?fbclid=IwAR1WcdyntoA1WC73mmUy3WWoUrmOnApf6miEia1S-vdVnXBhWj3uZHXxz64"
xml = urllib.request.urlopen(url)
x = xml.read().decode("utf-8")
root = ET.fromstring(x)
for child in root :
    for child2 in root :
        for item in child2.findall('item'):
            print(item.find('title').text)
            
    
#for type_tag in root.findall('rss/channel') :
    #value = type_tag.get('title')
    

#root = ET.parse(xml).getroot()
