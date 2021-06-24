import datetime 
import os
import pandas as pd
from re import search
from typing import Counter
from dotenv import load_dotenv

load_dotenv()

## Requesting API from user, similar to entering login information

API_KEY = os.getenv("API_KEY")
#print(len(API_KEY))

## Validating this API key can connect to the client (NYT) 

from pynytimes import NYTAPI

client = NYTAPI(API_KEY, parse_dates=True)
client

## Trying out the article search API

today = datetime.datetime.today()
week_ago = today - datetime.timedelta(days=7)

print(type(week_ago))

articles = client.article_search(
    query = "Bitcoin",
    results = 500,
    dates = {
        "begin": week_ago,
        "end": today
    },
    options = {
        "sort": "newest",
        #"sources": [
        #    "New York Times",
        #    "AP",
        #    "Reuters",
        #    "International Herald Tribune"
        #],
        # https://developer.nytimes.com/docs/articlesearch-product/1/overview
        #"news_desk": [
        #    "Politics"
        #],
        #"type_of_material": [
        #    "News Analysis"
        #]
    }
)

print(len(articles))
print(articles[0]["headline"]["main"])
print(articles[0]["web_url"])


### Notes
## Output: a ranking of a set of cryptocurrencies
    ## What does that output look like?
    ## How to query for multiple terms?
## Nice to have: Try to allow user to select dates
## Nice to have: emailed report (sendgrid)