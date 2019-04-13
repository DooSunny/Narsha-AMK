#pip install newspaper3
from newspaper import Article
#pip install beautifulsoup4
from bs4 import BeautifulSoup
import  urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

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
class news:
    url = "http://media.daum.net/rss/today/primary/all/rss2.xml"
    urls = list()
    def setarticle :
        artic = print("어떤 종류의 뉴스를 보시겠어요?(종합, 연예, 스포츠, 사회, 정치, 경제, 국제, 문화, 연예, IT-과학")
        if(artic == '종합'):
            url = "http://media.daum.net/rss/today/primary/all/rss2.xml"
        elif(artic == '연예'):
            url = "http://media.daum.net/rss/today/primary/entertain/rss2.xml"
        elif(artic == '스포츠'):
            url = "http://media.daum.net/rss/today/primary/sports/rss2.xml"
        elif(artic == '사회'):
            url = "http://media.daum.net/rss/part/primary/society/rss2.xml"
        elif(artic == '정치'):
            url = "http://media.daum.net/rss/part/primary/politics/rss2.xml"
        elif(artic == '경제'):
            url = "http://media.daum.net/rss/part/primary/economic/rss2.xml"
        elif(artic == '국제'):
            url = "http://media.daum.net/rss/part/primary/foreign/rss2.xml"
        elif(artic == '문화'):
            url = "http://media.daum.net/rss/part/primary/culture/rss2.xml"
        elif(artic == '연예'):
            url = "http://media.daum.net/rss/part/primary/entertain/rss2.xml"
        elif(artic == 'IT'):
            url = "http://media.daum.net/rss/part/primary/digital/rss2.xml"
        elif(artic == '과학'):
            url = "http://media.daum.net/rss/part/primary/digital/rss2.xml"
        elif(artic == 'IT-과학'):
            url = "http://media.daum.net/rss/part/primary/digital/rss2.xml"
        #주소의 xml을 불러온다
        xml = urllib.request.urlopen(url)
        #utf-8로 불러온다
        x = xml.read().decode("utf-8")
        root = ET.fromstring(x)
        titles = list()
        for child in root :
            for child2 in root :
                for item in child2.findall('item'):
                    list.append(item.find('title').text)
                    urls.append(item.find('link').text)
                    #뉴스 150자 까지 불러오기
        return titles
    # print(urls)
    def getnews(idx) :
        lang = Article(urls[int(idx)-1], language = 'ko')
        lang.download()
        lang.parse()
        return lang