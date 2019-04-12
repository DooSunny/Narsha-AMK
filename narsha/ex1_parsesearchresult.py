import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/"
keyword = "대구소프트웨어고등학교"

def wikipediaparser(soup):
    div = soup.find("div",{"class":"mw-parser-output"})
    description = div.find_all("p")

def main():
    with urllib.request.urlopen(url + keyword) as response:
     html = response.read()
     soup = BeautifulSoup(html, 'html.parser')
     wikipediaparser

if __name__ == '__main__':
    main()
