### CRYPTOTRENDS REPORT APP

import datetime 
import os
import pandas as pd
from re import search
from typing import Counter
from dotenv import load_dotenv
from pandas.core.frame import DataFrame

load_dotenv()

## Load API from dotenv

API_KEY = os.getenv("API_KEY")

## Validate that this API key can connect to the client (NYT) 

from pynytimes import NYTAPI

client = NYTAPI(API_KEY, parse_dates=True)
client

## Creating the cryptotrends report

today = datetime.datetime.today()
week_ago = today - datetime.timedelta(days=7)

print(type(week_ago))

btc_articles = client.article_search(
    query = "Bitcoin",
    results = 500,
    dates = {
        "begin": week_ago,
        "end": today
    },
    options = {
        "sort": "newest",

    }
)

eth_articles = client.article_search(
    query = "Ethereum",
    results = 500,
    dates = {
        "begin": week_ago,
        "end": today
    },
    options = {
        "sort": "newest",

    }
)

doge_articles = client.article_search(
    query = "Dogecoin",
    results = 500,
    dates = {
        "begin": week_ago,
        "end": today
    },
    options = {
        "sort": "newest",

    }
)

xrp_articles = client.article_search(
    query = "xrp",
    results = 500,
    dates = {
        "begin": week_ago,
        "end": today
    },
    options = {
        "sort": "newest",

    }
)

ada_articles = client.article_search(
    query = "Cardano",
    results = 500,
    dates = {
        "begin": week_ago,
        "end": today
    },
    options = {
        "sort": "newest",

    }
)

print("Cryptocurrency mentions in the NYTimes:",week_ago.strftime("%m/%d/%Y"),"through",today.strftime(("%m/%d/%Y")))
print("----------------------------------")

BTC_frq = len(btc_articles)

eth_frq = len(eth_articles)

doge_frq = len(doge_articles)

xrp_frq = len(xrp_articles)

ada_frq = len(ada_articles)

df = pd.DataFrame(data={"Cryptocurrencies": ["Ethereum","Bitcoin","Doge","Ripple","Cardano"],
                         "Number of mentions": [eth_frq, BTC_frq, doge_frq, xrp_frq, ada_frq]})

print(df.sort_values(by= ["Number of mentions"], inplace= True, ascending= False)) #> Figure out how to rank this
print("----------------------------------")

print("Number of BTC articles: ",BTC_frq)
if BTC_frq > 0:
    print("Latest: ",btc_articles[0]["headline"]["main"])
    print(btc_articles[0]["web_url"])
print("----------------------------------")

print("Number of ETH articles: ",eth_frq)
if eth_frq > 0:
    print("Latest: ",eth_articles[0]["headline"]["main"])
    print(eth_articles[0]["web_url"])
print("----------------------------------")

print("Number of Doge articles: ",doge_frq)
if doge_frq > 0:
    print("Latest: ",doge_articles[0]["headline"]["main"])
    print(doge_articles[0]["web_url"])

print("----------------------------------")

print("Number of Ripple articles: ",xrp_frq)
if xrp_frq > 0:
    print("Latest: ",xrp_articles[0]["headline"]["main"])
    print(xrp_articles[0]["web_url"])

print("----------------------------------")

print("Number of Cardano articles: ",ada_frq)
if ada_frq > 0:
    print("Latest: ",ada_articles[0]["headline"]["main"])
    print(ada_articles[0]["web_url"])


### To dos
## Output: a ranking of a set of cryptocurrencies
    ## What does that output look like?
## Test code (pytest?)
## Run through codeclimate
## Run it on a remote server (Travis?)
## Nice to have: emailed report (sendgrid), user inputs email?