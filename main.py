import requests
import json

headers = {
  'X-CMC_PRO_API_KEY' : '0bca2f73-0824-40b1-8303-823c1cb4daef',
  'Accepts' : 'application/json'
}

params = {
  'start'
  'limit' : '5',
  'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

json = requests.get(url, params=params, headers=headers).json()

print(json)