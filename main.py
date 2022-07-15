
from urllib import request
from flask import Flask, request
from Classes import nasdaq
import os

# create application instance from flask import
import json
app = Flask(__name__)
os.system('clear')

@app.route("/python_stocks/all", methods=['GET'])
def getStocks():
    data_obj = nasdaq.Stocks()
    # fetch all stocks in store
    return data_obj.fetch_all()

@app.route("/python_stocks/search", methods=['PUT'])
def getListOfStocks():
    # call webscaper function
    data_obj = nasdaq.Stocks()
    # check for body of request to be properly formatted
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        json = request.json['stock']
        # return data if passed checks
        if(type(json) == type([])):
            return data_obj.fetch(json), 200
        return 'Data not of type List', 400
    else:
        return 'Content type Error, must be of type json', 417


if __name__ == '__main__':
    app.run()