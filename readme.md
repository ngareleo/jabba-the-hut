# Jabba the Hut

### What is it?

It's a python service that tracks crypto token prices in the market

### Inspiration

I needed a trade helper to alert me about 
1 Changes in the market so that I can decide when to trade
2 Changes in the market so that I can know when to dump my asset or keep

The goal of the project is more to minimize losses than increase profits. I am a semi crypto-trader meaning that trading isn’t on my priority to-do list. However, I have witnessed my share of profits and many shares of losses to know it’s worth the time. Like a dangerous game of poker; very unpredictable and demanding. 

After a month in the whole thing, I can say it’s a good way of making money and even a better way of losing money. Therefore, I need an assistant.

My strategy is quite easy. I mark the prices at a set time and wait for a large fall in price. When I see a considerable rise I then jump on the train. I don’t know when it will take to reach the destination; it could be a day or even 10 minutes. The problem then comes in on telling when to jump or rather on which stop. I’ve seen my money gain about ksh1000 in a day and then drop in 10 minutes. That’s where my program joins the party. It’s like a conductor shouting stops along the way and whispering in my ear when it’s time to jump off. Of course, It will serve more purposes than that but that is its primary purpose.

Other purposes include keeping watch for my assets and signalling the best train to jump in. So, when I occasionally jump out at the safest time, I hop onto a safer much stable asset like Bitcoin where 20% changes in the price set me back very little money.

### Soft details

The system is made up of services running concurrently
The price tracking service
HTTP service

The system is not multiuser. I’m the sole user. 

What happens now? When I log into the system, http://127.0.0.1:6000, the HTTP server requests information from the price-tracking service.
