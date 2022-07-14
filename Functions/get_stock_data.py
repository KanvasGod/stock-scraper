import requests
from bs4 import BeautifulSoup

def output(array):
    url = 'https://www.google.com/finance/quote/'
    shipData = {}
    rawData = {}
    for x in array: 
        r = requests.get(url + x + ':NASDAQ')
        soup = BeautifulSoup(r.content, 'html.parser')
        scrape = soup.find('div', class_='eYanAe')
        content_value = scrape.find_all('div', class_='P6K39c')
        content_id = scrape.find_all('div', class_='mfs7Fc')
        rawData[x] = {"id": content_id, "value": content_value}

    for data in rawData:
        calcData = {}
        titleLen = len(rawData[data]["id"])

        for x in range(0, titleLen):
            calcData[rawData[data]["id"][x].text] = rawData[data]["value"][x].text
            
        shipData[data] = calcData

    return shipData