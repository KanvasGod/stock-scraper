# Stock Scraper

>Hi, welcome to my web-scarper build.
A usful tool for getting stock data, that other wise would'nt be easy to get in a free Api. All data is pulled from Google finance. with the caveat of only being able to pull from the NASDAQ and NYSE exchanges.

# API Usage

```http
GET  https://kanvasgod.pythonanywhere.com/python_stocks/all
```

```curl
PUT  https://kanvasgod.pythonanywhere.com/python_stocks/search
  Content-Type: application/json
  {
      "stock": ["SJR"]
  }
```
API does require a x-api-key in order to get data (open use keys coming soon) 

# Work in progress 

> I have many ideas on how to make this project even better, like expanding the sites it pulls data from. To adding more exchanges and adding open api keys for free use for anyone in need.

# Useful Links
[Google Finance](https://www.google.com/finance)

# License
Stock Scraper is licensed under the MIT license
