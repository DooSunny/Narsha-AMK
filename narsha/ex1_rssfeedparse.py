import xml.etree.ElementTree as ET
import urllib.request
from urllib import parse
#-*- coding:utf-8 -*-

s = input("검색어를 입력하세요 : ")
search = parse.quote(s)
#print(search)

#쿼리를 받아올 주소 (네이버 검색)
#url = "http://newssearch.naver.com/search.naver?where=rss&query="+search+"&field=0&nx_search_query=&nx_and_query=&nx_sub_query=&nx_search_hlquery=&is_dts=0"
#쿼리를 받아올 주소(다음 시사)

url = "https://media.daum.net/syndication/today_sisa.rss?fbclid=IwAR1WcdyntoA1WC73mmUy3WWoUrmOnApf6miEia1S-vdVnXBhWj3uZHXxz64"
#주소의 xml을 불러온다
xml = urllib.request.urlopen(url)
#utf-8로 불러온다
x = xml.read().decode("utf-8")

root = ET.fromstring(x)
for child in root :
    for child2 in root :
        for item in child2.findall('item'):
            print(item.find('title').text)