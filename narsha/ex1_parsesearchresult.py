#-*-coding: utf-8

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
# import re

def isResultExist(soup):
    return True
def wikipediaparser(soup):
    find_results = soup.find("div",{"class":"mw-parser-output"})
    if isResultExist(soup) == True:
        return None
    for i, data in enumerate(find_results):
        if i == 0:
            if str(data)[1] == 'p':
               pass
            else:
                 result = soup.select(".mw-parser-output p")[0].text
                 return result
        else: 
            if i%2 == 0 and str(data)[1] == 'p':
                result = data.text
                return result
    #select_results = soup.select(".mw-parser-output")
    #text = select_results[0].text
    return None

def main():
    url = "https://ko.wikipedia.org/wiki/"
    keyword = "대구소프트웨어고등학교" # it will be changed to user-text
    keyword = urllib.parse.quote(keyword)
    url = url + keyword    
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    desc = wikipediaparser(soup)
    if desc == None:
        print("WOW!") # exception code
    else:
        pass # giga-genie says something 


if __name__ == '__main__':
    main()
