import requests



resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')

print(resp.json())

#check for bitcoin prices
#build an algorithim


