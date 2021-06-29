### CRYPTOTRENDS REPORT APP

import datetime 
import os
import pandas as pd
from re import search
from typing import Counter
from dotenv import load_dotenv
from pandas.core.frame import DataFrame
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

## Load NYT API from dotenv

NYT_API_KEY = os.getenv("NYT_API_KEY", default="OOPS, please set env var called 'NYT_API_KEY'")

## Validate that this API key can connect to the client (NYT) 

from pynytimes import NYTAPI

client = NYTAPI(NYT_API_KEY, parse_dates=True)
client

## Allow user to input date range
while True:
  try:
      start_range = int(input("Please enter how many days (1-90) of cryptocurrency trends you'd like to include:"))
  except ValueError: 
      print("That's not a number!")
  else:
      if 1 <= start_range <= 90: 
          break
      else:
          print("Out of range. Try a number between 1-90")


today = datetime.datetime.today()
start_date = today - datetime.timedelta(days=start_range)
#start_date = today - datetime.timedelta(days=7)

## Query the API for the five cryptocurrency search terms (max of 100 results per coin)

btc_articles = client.article_search(
    query = "Bitcoin",
    results = 500,
    dates = {
        "begin": start_date,
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
        "begin": start_date,
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
        "begin": start_date,
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
        "begin": start_date,
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
        "begin": start_date,
        "end": today
    },
    options = {
        "sort": "newest",

    }
)

## Print a table of the five cryptocurrencies, ranked by number of mentions

print("Cryptocurrency mentions in the NYTimes:",start_date.strftime("%m/%d/%Y"),"through",today.strftime(("%m/%d/%Y")))
print("----------------------------------")

BTC_frq = len(btc_articles)

ada_frq = len(ada_articles)

doge_frq = len(doge_articles)

eth_frq = len(eth_articles)

xrp_frq = len(xrp_articles)

df = pd.DataFrame(data={"Cryptocurrencies": ["Bitcoin","Cardano","Doge","Ethereum","Ripple"],
                         "Number of mentions": [BTC_frq,ada_frq,doge_frq,eth_frq,xrp_frq]})

df.sort_values(by= ["Number of mentions"], inplace= True, ascending= False) 
print(df)

print("----------------------------------")

## Print the latest article for each cryptocurrency, if one is available, with the link to that article

def print_articles():

    print("Number of BTC articles: ",BTC_frq)
    if BTC_frq > 0:
        print("Latest: ",btc_articles[0]["headline"]["main"])
        print(btc_articles[0]["web_url"])
    print("----------------------------------")

    print("Number of Cardano articles: ",ada_frq)
    if ada_frq > 0:
        print("Latest: ",ada_articles[0]["headline"]["main"])
        print(ada_articles[0]["web_url"])

    print("----------------------------------")

    print("Number of Doge articles: ",doge_frq)
    if doge_frq > 0:
        print("Latest: ",doge_articles[0]["headline"]["main"])
        print(doge_articles[0]["web_url"])

    print("----------------------------------")

    print("Number of ETH articles: ",eth_frq)
    if eth_frq > 0:
        print("Latest: ",eth_articles[0]["headline"]["main"])
        print(eth_articles[0]["web_url"])
    print("----------------------------------")

    print("Number of Ripple articles: ",xrp_frq)
    if xrp_frq > 0:
        print("Latest: ",xrp_articles[0]["headline"]["main"])
        print(xrp_articles[0]["web_url"])
    print("----------------------------------")

print_articles()

## Enable emailed reports

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

## Set variables for Sendgrid Template

if BTC_frq > 0:
    btc_headline = btc_articles[0]["headline"]["main"]
    btc_url = btc_articles[0]["web_url"]
else:
    btc_headline = "No recent articles available"
    btc_url = ""

if eth_frq > 0:
    eth_headline = eth_articles[0]["headline"]["main"]
    eth_url = eth_articles[0]["web_url"]
else:
    eth_headline = "No recent articles available"
    eth_url = ""

if ada_frq > 0:
    ada_headline = ada_articles[0]["headline"]["main"]
    ada_url = ada_articles[0]["web_url"]
else:
    ada_headline = "No recent articles available"
    ada_url = ""

if doge_frq > 0:
    doge_headline = doge_articles[0]["headline"]["main"]
    doge_url = doge_articles[0]["web_url"]
else:
    doge_headline = "No recent articles available"
    doge_url = ""

if xrp_frq > 0:
    xrp_headline = xrp_articles[0]["headline"]["main"]
    xrp_url = xrp_articles[0]["web_url"]
else:
    xrp_headline = "No recent articles available"
    xrp_url = ""

now = datetime.datetime.now()
report_time = now.strftime("%m/%d/%y %I:%M:%S %p")        

## Format Sendgrid template - this must match the test data structure

template_data = {
    "human_friendly_timestamp": "July 26th, 2021 8:00 AM",
    "btc_frq": BTC_frq,
    "eth_frq": eth_frq,
    "ada_frq": ada_frq,
    "xrp_frq": xrp_frq,
    "doge_frq": doge_frq,
    "btc_headline": btc_headline,
    "eth_headline": eth_headline,
    "ada_headline": ada_headline,
    "xrp_headline": xrp_headline,
    "doge_headline":doge_headline,
    "btc_url": btc_url,
    "eth_url": eth_url,
    "ada_url": ada_url,
    "xrp_url": xrp_url,
    "doge_url": doge_url
}

client = SendGridAPIClient(SENDGRID_API_KEY)

## Validate sendgrid is working

print("CLIENT:", type(client))
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
message.template_id = SENDGRID_TEMPLATE_ID
message.dynamic_template_data = template_data
print("MESSAGE:", type(message))
try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as err:
    print(type(err))
    print(err)
