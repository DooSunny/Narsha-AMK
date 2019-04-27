#-*-coding: utf-8

from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import MicrophoneStream as MS
import call_stt as genie

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
    keyword = genie.Call()
    url = url + quote(keyword)
   #  url = urllib.parse.urlparse(url)
    # url = urllib.parse.parse_qs(url.query)
    # urllib.parse.urlencode(url, encoding='UTF-8', doseq = True)
    try:
        print("url open")
        response = urlopen(url)
        print("url open complete")
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        desc = wikipediaparser(soup)
        print(desc)
       
        if desc == None:
            print("오류코드 1", output_file) # exception code
        else:
            genie.getText2VoiceStream(desc, output_file)# giga-genie says something 
    except Exception as e:
        genie.getText2VoiceStream("오류코드 2",output_file) # giga-genie says something
        print(e)
    MS.play_file(output_file)

if __name__ == '__main__':
    main()
