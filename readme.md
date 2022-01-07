starting_point => A point we start tracking an asset (Coin)


As we track the prices, we wait for a drop in price, If the price dips to about 70% potential_profit_point

we then alert, user
if the price rises past a trigger_point we start the sale

The sale begins creating a buy_session

We continue tracking the price, 
    if the price drops, we watch it before it reaches the drop_first_caution_point, as the price continues to fall we finally reach the final_drop_lose_point 
        these two points are optional
    if the price rises, we watch it until we reach the profit_ceiling,
        if the price falls, we wait until it reaches the profit_sell_profit_point
        when the price reaches, the profit_sell_caution_point, we alert
    When we sell, we create a starting_point


