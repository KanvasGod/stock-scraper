from dotenv import load_dotenv
from urllib import request
from flask import Flask, request, render_template
from Classes import stock_look_up
import os

# create application instance from flask import
import json

project_folder = os.getcwd()
app = Flask(__name__)
load_dotenv(os.path.join(project_folder, '.env'))

os.system('clear')

apiKey = os.environ.get('API_KEY')

@app.route("/python_stocks/all", methods=['GET'])
def getStocks():
    try: 
        auth = request.headers.get("X-Api-Key")
    except Exception as e:
        return "Incorrect API Headers", 401

    if auth == apiKey:
        data_obj = stock_look_up.Stocks()
        data_obj.update_all()
        # fetch all stocks in store
        return data_obj.fetch_all()
    else:
        return "unauthorized", 401

@app.route("/python_stocks/search", methods=['PUT'])
def getListOfStocks():

    try:
        auth = request.headers.get("x-api-key")
    except Exception as e:
        return "Incorrect API Headers", 401

    if auth == apiKey:
        # call webscaper function
        data_obj = stock_look_up.Stocks()
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
    return render_template('error.html')

if __name__ == '__main__':
    app.run()