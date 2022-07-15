import requests
from bs4 import BeautifulSoup
import json

def output(array):
    # website to scrape
    url = 'https://www.google.com/finance/quote/'
    # shipData  is what this function will return
    shipData = {}
    # rawdata is used to store webpage data
    rawData = {}

    for x in array:
        # scrape webpage and return data if available
        try:
            r = requests.get(url + x.upper() + ':NASDAQ')
            soup = BeautifulSoup(r.content, 'html.parser')
            scrape = soup.find('div', class_='eYanAe')
            content_value = scrape.find_all('div', class_='P6K39c')
            content_id = scrape.find_all('div', class_='mfs7Fc')
            
            if content_id != type('NoneType'):
                # save data to rawData
                rawData[x.upper()] = {"id": content_id, "value": content_value}
        except Exception as e:
            print(e)

    for data in rawData:
        # building shipData dict
        calcData = {}
        titleLen = len(rawData[data]["id"])

        for x in range(0, titleLen):
            # save title & value
            calcData[rawData[data]["id"][x].text] = rawData[data]["value"][x].text
            
        shipData[data] = calcData

    return shipData