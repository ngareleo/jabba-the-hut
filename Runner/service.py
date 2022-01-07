from JabbaAPI import JabbaRequestAPI
from Runner import settings
from time import sleep
from models import Point, Watchpoint
from datetime import datetime
from settings import Settings


class TradeService:

    def __init__(self):

        # our cache
        self.jabba_api = JabbaRequestAPI(fav_assets=settings.my_assets)
        self.user_settings = settings.DatabaseConnector().get_user_settings()
        self.service_settings = Settings()

        ###############################################

        self.current_watchpoint = self.service_settings.get_current_watchpoint()  # we store ids only
        self.cached_points = self.service_settings.get_cached_points(self.current_watchpoint)
        self.start_service()

    def start_service(self):
        while True:
            asset_current_prices = self.jabba_api.request_prices()
            # check if there is a watchpoint
            for asset in asset_current_prices:

                if not self.current_watchpoint:
                    # create the wp
                    this_point_price = asset.get('price_usd')
                    prev_point = self.get_asset_price_diff(None if len(self.cached_points) else self.cached_points[0],
                                                           this_point_price)

                    # we need to get information from the db
                    temp_watchpoint = Watchpoint(
                        init_time=datetime.now(),
                        point_price=asset.get('price_usd'),
                        price_change_from_prev=prev_point,
                        price_change_from_watchpoint=None,
                        my_watchpoint=None

                    )

                    self.current_watchpoint = temp_watchpoint
                    self.service_settings.set_current_watchpoint(temp_watchpoint)

                else:
                    # there's a watchpoint
                    this_point_price = asset.get('price_usd')
                    prev_point = self.get_asset_price_diff(None if len(self.cached_points) else self.cached_points[0],
                                                           this_point_price)
                    change_from_watchpoint = self.get_price_from_watchpoint(this_point_price)
                    # we create a normal point
                    asset_point_obj = Point(
                        init_time=datetime.now(),
                        point_price=asset.get('price_usd'),
                        price_change_from_prev=prev_point,
                        price_change_from_watchpoint=change_from_watchpoint,
                        my_watchpoint=self.current_watchpoint
                    )
                    self.cached_points.append(asset_point_obj)

                    # save the point in db
            sleep(10)

    def get_asset_price_diff(self, price_then_uuid, price_now):

        prev_point = self.service_settings.get_point_price(price_then_uuid)
        return price_now - prev_point

    def get_price_from_watchpoint(self, price_now):
        prev_point = self.service_settings.get_point_price(self.current_watchpoint.get('_id'))
        return price_now - prev_point

if __name__ == '__main__':
    sett = Settings()
    ts = TradeService()





