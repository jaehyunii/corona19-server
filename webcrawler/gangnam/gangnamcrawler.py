from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.parse
import re

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
driver.get('https://www.gangnam.go.kr/path.htm')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

def parser(str) :
    items = re.findall(r"-", str)
    
    for idx, element in enumerate(items):
        tmp = re.split(' ', element)
        date = tmp[1]
        if len(tmp[2]) != 0:
            time = tmp[2]
            tmp = [str(datetime.now().year) + items[current], time[0], name]


def doCrawling() :
    print("강남구 크롤링 시작")
    result = []
    soup = BeautifulSoup(html, 'html.parser')
    target = soup.find('div', {'id':'tab-1'})
    [tag.decompose() for tag in target.find_all('td', {'colspan':'6'})]
    tds = target.find_all('td')

    if tds is not None:
        for idx, item in enumerate(tds):
            if(idx != len(tds) - 1):
                result.append(parser(item.string))
        for element in result :
            print(element)
        


#For Testing
doCrawling() 

print("강남구 크롤링 종료")