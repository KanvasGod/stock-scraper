
from urllib import request
from flask import Flask
import requests
# create application instance from flask import
import json
app = Flask(__name__)

@app.route("/python_stocks/all", methods=['GET'])
def getStocks():
    return "he"

@app.route("/python_stocks/search", methods=['put'])
def getListOfStocks():
    data = requests.get('https://www.google.com/finance/quote/AAPL:NASDAQ')
    print(data.content)
    return "hello world"



if __name__ == '__main__':
    app.run()