import requests


#fetch data
resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')

print(resp.json())

#check for prices
#build an algorithim


