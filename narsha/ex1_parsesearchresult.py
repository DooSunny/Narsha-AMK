#-*-coding: utf-8

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
# import re

def wikipediaparser(soup): # func about parse wikipedia
    find_results = soup.find("div",{"class":"mw-parser-output"}) # find information div
    for i, data in enumerate(find_results): 
        if i == 0: # detect wrong data
            if str(data)[1] == 'p': # is there wrong data?
               pass
            else: # if do this line, it is right data
                 result = soup.select(".mw-parser-output p")[0].text
                 return result
        else: # where is right data...
            if i%2 == 0 and str(data)[1] == 'p':
                result = data.text
                return result
    return None

def main():
    url = "https://ko.wikipedia.org/wiki/"
    keyword = "대구소프트웨어고등학교" # it will be changed to user-text
    keyword = urllib.parse.quote(keyword)
    url = url + keyword    
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        desc = wikipediaparser(soup)
        if desc == None:
            print("Something Wrong...") # exception code
        else:
            pass # giga-genie says something 
    except:
        print("No search Result") # giga-genie says something


if __name__ == '__main__':
    main()
