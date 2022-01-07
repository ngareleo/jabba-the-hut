import pymongo
from models import Watchpoint
my_assets = [
    {
        'name': 'Bitcoin',
        'asset_id': 'BTC'
    },
    {
        'name': 'Binance Coin',
        'asset_id': 'BNB'
    },
    {
        'name': 'Ethereum',
        'asset_id': 'ETH'
    },
    {
        'name': 'Cosmos',
        'asset_id': 'ATOM'
    },
    {
        'name': 'Chainlink',
        'asset_id': 'LINK'
    },
    {
        'name': 'Uniswap',
        'asset_id': 'UNI'
    },
    {
        'name': 'Dogecoin',
        'asset_id': 'DOGE'
    },
    {
        'name': 'Ripple',
        'asset_id': 'XRP'
    },
    {
        'name': 'ZCash',
        'asset_id': 'ZEC'
    },
    {
        'name': 'Cardano',
        'asset_id': 'ADA'
    },
    {
        'name': 'Polkadot',
        'asset_id': 'DOT'
    },
    {
        'name': 'Miota',
        'asset_id': 'IOTA'
    },
    {
        'name': 'Litecoin',
        'asset_id': 'LTC'
    },
    {
        'name': 'Stellar Lumens',
        'asset_id': 'XLM'
    },
    {
        'name': 'TRON',
        'asset_id': 'TRX'
    },
    {
        'name': 'Bitcoin Cash',
        'asset_id': 'BCH'
    },
    {
        'name': 'Ripple',
        'asset_id': 'XRP'
    },
    {
        'name': 'Filecoin',
        'asset_id': 'FIL'
    },
    {
        'name': 'Qtum',
        'asset_id': 'QTUM'
    },
    {
        'name': 'Dash',
        'asset_id': 'DASH'
    },
]


class DatabaseConnector:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.jabba_db = self.mongo_client['jabbadb']

    def get_user_settings(self):
        return self.jabba_db['user-settings']

    def get_point_collection(self):
        return self.jabba_db['points']

    def get_watchpoints(self):
        return self.jabba_db['starting-points']


class Settings:
    def __init__(self):
        # collection
        self._watchpoint_collection = DatabaseConnector().get_watchpoints()
        self._points = DatabaseConnector().get_point_collection()
        # deserialize the watchpoints
        self._current_watchpoint = None  # watchpoint id

    def get_cached_points(self, watchpoint):
        if watchpoint is None:
            return []

        query = {
            "my_watchpoint": str(watchpoint)
        }
        points = [_.get('_id') for _ in self._points.find(query).sort("init_time", -1)]
        return points

    def get_current_watchpoint(self):
        # read from database
        query = {
            "date_init": -1
        }
        latest_wp = self._watchpoint_collection.find().sort(query).limit(1)
        self._current_watchpoint = latest_wp
        return self._current_watchpoint

    def set_current_watchpoint(self, watchpoint: Watchpoint):
        self._watchpoint_collection.insert_one(watchpoint.__dict__)
        self._current_watchpoint = watchpoint

    def get_point_price(self, uuid):
        query = {
            "_id": str(uuid)
        }
        prev_point_cursor = self._points.find(query)
        prev_point = [_ for _ in prev_point_cursor][0]
        return float(prev_point.get('point_price'))






