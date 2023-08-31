import time
import os
from signature import get_kraken_signature
import requests

# Read Kraken API key and secret stored in environment variables
api_url = "https://api.kraken.com"
api_key = os.environ['API_KEY_KRAKEN']
api_sec = os.environ['API_SEC_KRAKEN']

# Attaches auth headers and returns results of a POST request
def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    # get_kraken_signature() 
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((api_url + uri_path), headers=headers, data=data)
    return req

# Construct the request to buy and print the result
buy = kraken_request('/0/private/AddOrder', {
    "nonce": str(int(1000*time.time())),
    "ordertype": "limit",
    "type": "buy",
    "volume": 0,
    "pair": "XBTUSD",
    "price": 10
}, api_key, api_sec)

print(buy.json())

sell = kraken_request('/0/private/AddOrder',{
  "nonce": str(int(1000*time.time())),
  "ordertype": "limit",
  "type": "sell",
  "volume":0,
  "pair":"XBTUSD",
  "price":10
},api_key , api_sec)
print(sell.json())