
#pip install beautifulsoup4
from bs4 import BeautifulSoup
import  urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import random
#url = "https://media.daum.net/syndication/today_sisa.rss"
# 종합 http://media.daum.net/rss/today/primary/all/rss2.xml
# 연예 http://media.daum.net/rss/today/primary/entertain/rss2.xml
# 스포츠 http://media.daum.net/rss/today/primary/sports/rss2.xml
# 사회 http://media.daum.net/rss/part/primary/society/rss2.xml
# 정치 http://media.daum.net/rss/part/primary/politics/rss2.xml
# 경제 http://media.daum.net/rss/part/primary/economic/rss2.xml
# 국제 http://media.daum.net/rss/part/primary/foreign/rss2.xml
# 문화·생활 http://media.daum.net/rss/part/primary/culture/rss2.xml
# 연예 http://media.daum.net/rss/part/primary/entertain/rss2.xml
# IT·과학 http://media.daum.net/rss/part/primary/digital/rss2.xml
class newspaperdaum:
    url = "http://media.daum.net/rss/today/primary/all/rss2.xml"
    urls = list()
    def setarticle(self,) :
        
        # if('종합' in artic):
        #     self.url = "http://media.daum.net/rss/today/primary/all/rss2.xml"
        # elif('연예' in artic):
        #     self.url = "http://media.daum.net/rss/today/primary/entertain/rss2.xml"
        # elif(artic in '스포츠'):
        #     self.url = "http://media.daum.net/rss/today/primary/sports/rss2.xml"
        # elif(artic in '사회'):
        #     self.url = "http://media.daum.net/rss/part/primary/society/rss2.xml"
        # elif(artic in '정치'):
        #     self.url = "http://media.daum.net/rss/part/primary/politics/rss2.xml"
        # elif(artic in '경제'):
        #     self.url = "http://media.daum.net/rss/part/primary/economic/rss2.xml"
        # elif(artic in '국제'):
        #     self.url = "http://media.daum.net/rss/part/primary/foreign/rss2.xml"
        # elif(artic in '문화'):
        #     self.url = "http://media.daum.net/rss/part/primary/culture/rss2.xml"
        # elif(artic in '연예'):
        #     self.url = "http://media.daum.net/rss/part/primary/entertain/rss2.xml"
        # elif(artic in 'IT'):
        #     self.url = "http://media.daum.net/rss/part/primary/digital/rss2.xml"
        # elif(artic in '과학'):
        #     self.url = "http://media.daum.net/rss/part/primary/digital/rss2.xml"
        # elif(artic in 'IT-과학'):
        #     self.url = "http://media.daum.net/rss/part/primary/digital/rss2.xml"
        #주소의 xml을 불러온다
        xml = urllib.request.urlopen(self.url)
        #utf-8로 불러온다
        x = xml.read().decode("utf-8")
        root = ET.fromstring(x)
        titles = list()
        for child in root :
            for child2 in root :
                for item in child2.findall('item'):
                    titles.append(item.find('title').text)
                    self.urls.append(item.find('link').text)
                    #뉴스 150자 까지 불러오기
        #for문 안에 넣어서 사용
        return titles
    # print(urls)
    def getnews(self) :
        url = randomurl = random.choice(urls)
        response=urllib.request.urlopen(url)
        soup=BeautifulSoup(response,'html.parser')
        results = soup.select("section > p")
        return results