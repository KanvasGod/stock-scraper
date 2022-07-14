
from urllib import request
from flask import Flask
from Classes import nasdaq

# create application instance from flask import
import json
# app = Flask(__name__)

data = nasdaq.Stocks()
print(data.fetch(['AAPL', 'MSFT', 'AMZN']))

# @app.route("/python_stocks/all", methods=['GET'])
# def getStocks():
#     return "he"

# @app.route("/python_stocks/search", methods=['PUT'])
# def getListOfStocks():
#     data = nasdaq.Stocks()
#     return data.fetch(['AAPL'])


# if __name__ == '__main__':
#     app.run()