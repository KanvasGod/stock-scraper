from Functions import get_stock_data
from dotenv import load_dotenv, find_dotenv
from urllib import request
from flask import Flask, request, render_template
from Classes import nasdaq
import os

# create application instance from flask import
import json
app = Flask(__name__)
load_dotenv(find_dotenv())
os.system('clear')

@app.route("/python_stocks/all", methods=['GET'])
def getStocks():
    try: 
        auth = request.headers.get("X-Api-Key")
    except Exception as e:
        return "Incorrect API Headers", 401

    apiKey = os.environ.get('API_KEY')

    if auth == apiKey:
        data_obj = nasdaq.Stocks()
        data_obj.update_all()
        # fetch all stocks in store
        return data_obj.fetch_all()
    else:
        return "unauthorized", 401

@app.route("/python_stocks/search", methods=['PUT'])
def getListOfStocks():

    try: 
        auth = request.headers.get("X-Api-Key")
    except Exception as e:
        return "Incorrect API Headers", 401

    apiKey = os.environ.get('API_KEY')

    if auth == apiKey:
        # call webscaper function
        data_obj = nasdaq.Stocks()
        data_obj.update_all()
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

    else:
        return "unauthorized", 401

@app.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return render_template("index.html"), 404


if __name__ == '__main__':
    app.run()