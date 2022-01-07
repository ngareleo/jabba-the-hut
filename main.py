
import requests
url = 'https://rest.coinapi.io/v1/assets?filter_asset_id=BTC;ETH;ATOM'
headers = {'X-CoinAPI-Key': '0AD863BB-C207-414C-A510-5503AFCDB339'}
response = requests.get(url, headers=headers)

for item in response.json():
    amount = "${:,.2f}".format(item.get('price_usd'))
    print(f"{item.get('asset_id')} {item.get('name')} {amount}")