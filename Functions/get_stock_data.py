import requests
from bs4 import BeautifulSoup

def output(array):
    # website to scrape
    url = 'https://www.google.com/finance/quote/'
    # shipData  is what this function will return
    shipData = {}
    # rawdata is used to store webpage data
    rawData = {}
    # stock exchanges
    exchanges = ['NASDAQ', 'NYSE']

    for x in array:
        # scrape webpage and return data if available
        for index in exchanges:
            newUrl = f"{url}{x.upper()}:{index}"
            try:

                r = requests.get(newUrl)
                soup = BeautifulSoup(r.content, 'html.parser')
                scrapeNull = soup.find('div', class_='b4EnYd')
                scrapeValue = scrape = soup.find('div', class_='eYanAe')
                if scrapeNull == None:
                    print(x, index, "No responce detected")

                if scrapeValue != None:
                    content_id = scrape.find_all('div', class_='mfs7Fc')
                    content_value = scrapeValue.find_all('div', class_='P6K39c')
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