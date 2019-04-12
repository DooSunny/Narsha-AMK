#-*-coding: utf-8

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
# import re

def wikipediaparser(soup):
    results = soup.select(".mw-parser-output p")
    text = results[0]
    return text
def main():
    url = "https://ko.wikipedia.org/wiki/"
    keyword = "C++" # it will be changed to user-text
    url = url + keyword    
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    desc = wikipediaparser(soup)
    if desc == []:
        pass # will insert exception code


if __name__ == '__main__':
    main()
