from ast import Try
from Functions import get_stock_data
from datetime import datetime, timedelta
import os
import json

class Stocks(object):
    def __init__(self):
        self.storeId = 'nasdaq'

    def fetch_all(self):
        # Get all stocks in store
        try:
            with open('store/stocks.json', 'r') as latest_file:
                stockData = json.load(latest_file)
                return stockData

        except Exception as e:
            print(e)
            return {}


    def update_all(self):
        # void function
        # Update all items in Store.
        current_time = datetime.now()
        future_date = None
        try:
            date = open('store/update_timer.json', 'r')
            read = json.loads(date.read())
            future_date = datetime.fromisoformat(read["future_date"])
        except Exception as e:
            print("future_date failed to post",e)
        
        try:
            
            if(future_date and future_date < current_time):
                with open('store/stocks.json', 'r') as latest_file:
                    stockData = json.load(latest_file)
                    # get all stocks in store
                    stocks = stockData.keys()
                    stocksUpdate = get_stock_data.output(stocks)
                    for ticker in stocks:
                        stockData[ticker] = stocksUpdate[ticker]
                    # save back to store
                    f = open('store/stocks.json', 'w')
                    f.write(json.dumps(stocksUpdate, indent=4))
                    f.close()
                    

            if(future_date == None or  future_date < current_time):
                # create new update timer
                new_date = timedelta(days= 1)
                future_date = current_time + new_date
                f = open('store/update_timer.json', 'w')
                f.write(json.dumps({
                    "future_date": future_date.__str__()
                }, indent=4))
                f.close()

        except Exception as e:
            print(e)
        

    def fetch(self, array):
        # check for data in store, if data doesn't exist webscape and add to store.
        try:

            with open('store/stocks.json', 'r') as latest_file:
                stockData = json.load(latest_file)
                # create an new array by comparing store data
                newArray = [i for i in array if i not in stockData.keys()]
                # scrape missing data
                ticker_data = get_stock_data.output(newArray)

                for ticker in ticker_data.keys():
                    if ticker not in stockData.keys():
                        stockData[ticker] = ticker_data[ticker]
                # save new stock data
                f = open('store/stocks.json', 'w')
                f.write(json.dumps(stockData, indent= 4))
                f.close()
                        
                return stockData

        except Exception as e:
            print(e)
            # create new file
            stockData = get_stock_data.output(array)
            stockData = json.dumps(stockData, indent=4)
            f = open('store/stocks.json', 'w')
            f.write(stockData)
            f.close()