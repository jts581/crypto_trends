import datetime
import os
import pandas as pd
from re import search
from typing import Counter
from dotenv import load_dotenv

load_dotenv()

## Requesting API from user, similar to entering login information

API_KEY = os.getenv("API_KEY")
print(len(API_KEY))

## Validating this API key can connect to the client (NYT) 

from pynytimes import NYTAPI

client = NYTAPI(API_KEY, parse_dates=True)
client

## Returning the different APIs available from the client

from pprint import pp, pprint

pprint([method for method in dir(client) if not method.startswith("_")])

## Since we're trying to identify trends in a set of cryptocurrencies
## ...we'll count mentions in the 'top_stories' articles 
## ...top_stories can be filtered by section, most_viewed and most_shared can't
## ...and we'll filter top_stories by the "business" section    

## Set a variable for current day
current_date = datetime.datetime.today()
print(current_date)

start_date = datetime.date(current_date)
number_of_days = 5
date_list = []
for day in range(number_of_days):
  a_date = (start_date + datetime.timedelta(days = day)).isoformat()
  date_list.append(a_date)

stories = client.article_search(dates= {date_list})

(len(stories))

## Return the first story, its type (it's a dict), and its keys

story = stories[0]
pprint(type(story))
pprint(story.keys())
#pprint(story)S

## Return the title, abstract, des_facet, and org_facet
#pprint(story["title"])
#pprint(story["abstract"])
#pprint(story["des_facet"])
#pprint(story["org_facet"])

## Return the titles of articles that have a certain word in their
## ...title, abstract, des_facet, or org_facet

search_phrase = "bitcoin" #> Just a thought, we could even turn this into a user input

filtered_stories = []
for item in biz_stories:
    if search_phrase in (item["abstract"] or item["title"] or item["des_facet"] or item["org_facet"]):
        filtered_stories.append(item)
#> Is this or statement working?
#> Is this double counting?

print(len(filtered_stories))

for s in filtered_stories:
    print(s["abstract"])
