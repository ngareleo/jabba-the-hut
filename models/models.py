class User:

    def __init__(self, fav_assets):
        self.favorite_assets = fav_assets  # extract from a database file


class Point:

    def __init__(self,
                 init_time,
                 point_price,
                 price_change_from_prev=None,
                 price_change_from_watchpoint=None,
                 my_watchpoint=None):
        # id is automatically added by mongo
        self.init_time = init_time
        self.point_price = point_price
        self.price_change_from_prev = price_change_from_prev
        self.price_change_from_watchpoint = price_change_from_watchpoint
        self.my_watchpoint = my_watchpoint


class Watchpoint(Point):

    def __init__(self,
                 init_time,
                 point_price,
                 price_change_from_prev=None,
                 price_change_from_watchpoint=None,
                 my_watchpoint=None
                 ):
        super().__init__(init_time,
                         point_price,
                         price_change_from_prev,
                         price_change_from_watchpoint,
                         my_watchpoint
                         )
        self.point_valid = False
