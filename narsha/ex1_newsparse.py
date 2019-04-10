#pip install newspaper3
from newspaper import Article
#pip install beautifulsoup4
from bs4 import BeautifulSoup
import  urllib.request
import urllib.parse

#네이버 뉴스 주소
url = "https://news.naver.com"
#페이지 정보 불러오기
response=urllib.request.urlopen(url)
soup=BeautifulSoup(response,'html.parser')

#네이버 뉴스의 헤더뉴스 정보 불러오기
results = soup.select(".hdline_article_tit a")
#헤더뉴스 url목록을 포함하는 배열 생성
urls = list()
for result in results:
    #배열에 헤더라인 뉴스의 주소 저장
    urls.append(url+result.attrs["href"])
for url in urls :
    #한국어와 뉴스 주소 불러오기
    lang = Article(url, language = 'ko')
    lang.download()
    lang.parse()
    #뉴스 제목
    print(lang.title+"\n")
    #뉴스 150자 까지 불러오기
    print(lang.text[:150]+"\n")
    print("다음 뉴스\n")
#참고자료
#뱅뱅님의 블로그 [Python] 20171117 crawling - 네이버 뉴스 헤드라인 가져오기
# https://m.blog.naver.com/PostView.nhn?blogId=kbw0104&logNo=221142104174&proxyReferer=https%3A%2F%2Fwww.google.com%2F
#EXCELSIOR님의 블로그 Newspaper 모듈을 이용하여 뉴스 기사 크롤링하기
#https://excelsior-cjh.tistory.com/92