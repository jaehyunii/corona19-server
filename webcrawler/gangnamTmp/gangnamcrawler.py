from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import requests
import time


def doCrawling() :
    print("강남구 크롤링 시작")
    with urllib.request.urlopen("https://www.gangnam.go.kr/path.htm") as response:
        result = []
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        
        with open("a.txt", "w", -1, 'utf-8') as f :
            f.write(str(soup))
            f.close()
        print(soup)
        target = soup.find('div', {'id':'tab-1'})
        tds = target.find_all('td')
        if tds is not None:
            for idx, item in enumerate(tds) :
                if(idx != len(tds) - 1) :
                    result.append(item.string)
            


doCrawling()