import threading
import requests
import json
import os
import logging

#here I will list the currencies and then 
# add a function to be able to download the currency data from floatrates
rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", 
         "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", 
         "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", 
         "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", 
         "SEK", "CHF", "THB", "TTD"]
def download_currency(base):
    url = f"https://www.floatrates.com/daily/{base}.json"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        os.makedirs("data", exist_ok=True)
        with open(f"data/{base}.json", "w") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Successfully downloaded data for {base}")
    except Exception as e:
        logging.error(f"Failed to download data for {base}: {str(e)}")
#here I have the logging info from sidequest 1
#here I will do the threading for the currencies 
def run_quest1():
    threads = [threading.Thread(target=download_currency, args=(currency,)) for currency in rates]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    run_quest1()
    
       