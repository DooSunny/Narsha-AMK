#-*-coding: utf-8

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ex1_call_stt_tts as genie

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
    output_file = "testtts.wav"
    url = "https://ko.wikipedia.org/wiki/"
    keyword = genie.getVoice2Text()
    keyword = urllib.parse.quote(keyword)
    url = url + keyword    
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        desc = wikipediaparser(soup)
        print(desc)
       
        if desc == None:
            print("Something Wrong...") # exception code
        else:
            genie.getText2VoiceStream(desc, output_file)# giga-genie says something 
    except:
        print("No search Result") # giga-genie says something



if __name__ == '__main__':
    main()
