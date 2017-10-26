"""
Data source: Bitfinex
Symbols rate limit: 5 requests/min
Ticker rate limit: 60 requests/min
Stats rate limit: 10 requests/min
"""

import requests
import time
import pandas as pd
import json

url_symbols = "https://api.bitfinex.com/v1/symbols"
url_ticker = "https://api.bitfinex.com/v1/pubticker/"
url_stats = "https://api.bitfinex.com/v1/stats/"
ticker = "btcusd"

all_symbols = [
"btcusd", "ltcusd", "ltcbtc", "ethusd", "ethbtc", "etcbtc", "etcusd", "rrtusd",
"rrtbtc", "zecusd", "zecbtc", "xmrusd", "xmrbtc", "dshusd", "dshbtc", "bccbtc",
"bcubtc", "bccusd", "bcuusd", "xrpusd", "xrpbtc", "iotusd", "iotbtc", "ioteth",
"eosusd", "eosbtc", "eoseth", "sanusd", "sanbtc", "saneth", "omgusd", "omgbtc",
"omgeth", "bchusd", "bchbtc", "bcheth", "neousd", "neobtc", "neoeth", "etpusd",
"etpbtc", "etpeth", "qtmusd", "qtmbtc", "qtmeth", "bt1usd", "bt2usd", "bt1btc",
"bt2btc", "avtusd", "avtbtc", "avteth", "edousd", "edobtc", "edoeth", "bg1usd",
"bg2usd", "bg1btc", "bg2btc", "btgusd", "btgbtc"]

selected_symbols = [
"btcusd", "ltcusd", "ethusd", "xrpusd", "iotusd", "omgusd"]

df = pd.DataFrame(columns=selected_symbols)

length = range(120)

for i in length:
    responses = []
    for symbol in selected_symbols:
        resp_ticker = requests.get(url_ticker + symbol)
        responses.append(json.loads(resp_ticker.text))
        # print(resp_ticker.text)
    # df = pd.concat([df, pd.Series(responses)], axis = 1)
    if(i == 0):
        df.loc[0] = responses
    else:
        df.loc[df.index.max() + 1] = responses
    if(i % 10 == 0):
        print("{:.1%} of time elapsed.".format(i/len(length)))
    if(i != length):
        time.sleep(10)


# resp_symbols = requests.get(url_symbols)
# resp_stats = requests.get(url_stats + ticker)
