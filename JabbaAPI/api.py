import requests


class JabbaRequestAPI:

    def __init__(self, fav_assets):
        self.router = KeyRouter()
        self.fav_assets = [item.get('asset_id') for item in fav_assets]
        self.url = 'https://rest.coinapi.io/v1/assets?filter_asset_id='
        for asset in self.fav_assets:
            self.url += f'{asset};'

    def request_prices(self):
        print(self.url)
        asset_data = requests.get(self.url, headers=self.router.get_key()).json()
        return asset_data


class KeyRouter:
    keys = {
        "ngareoel@gmail.com": "C59FD243-BC36-46F1-9D1E-A093F6479315",
        "ngarioel@gmail.com": "5C670848-3FA6-4D3D-A0EB-D070B8A35CF5",
        "dev.ngari@gmail.com": "5C670848-3FA6-4D3D-A0EB-D070B8A35CF5",
        "ngarimwenda@gmail.com": "0AD863BB-C207-414C-A510-5503AFCDB339",
        "vegew52655@rubygon.com": "F7BF4D14-6EE5-4280-A1BF-528777FF639F",
        "gfsnmpefnd@frederictonlawyer.com": "DFF371F6-B1F7-44C6-B0BB-293497892093"
    }

    # I really need more keys

    counter = 0

    def get_key(self):
        key_header = {'X-CoinAPI-Key': list(self.keys.values())[self.counter]}
        self.counter += 1
        if self.counter == len(self.keys):
            self.counter = 0
        return key_header
