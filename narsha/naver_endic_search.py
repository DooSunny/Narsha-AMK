from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.request import urlopen

def meaning_find(soup):
    find_span = soup.find("span", {"class":"fnt_k05"})

    if find_span == None:
        return "Not Result"
    else:
        return find_span.text

def main():
    output_file = "testtts.wav"
    url = "https://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query="
    query = input()
    url = url + quote(query)

    try:
         print("url open")
         response = urlopen(url)
         print("url open complete")
         html = response.read()
         soup = BeautifulSoup(html, 'html.parser')
         desc = meaning_find(soup)
         print(desc)
    except Exception:
        print("Unknown Error")

if __name__ == '__main__':
    main()