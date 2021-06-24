import os
from re import search
from dotenv import load_dotenv

load_dotenv()

## Requesting API from user, similar to entering login information

from getpass import getpass 
API_KEY = getpass("API Key: ") 
# Note that entering an API in terminal (at least Git Bash) is difficult
# ...because user can't see what they're entering.
# ...see here for details: https://stackoverflow.com/questions/13399315/cant-type-password-in-git-bash

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
## ...top_stories can be filtered by section, most_viewed and most_shared can not
## ...and we'll filter top_stories by the "business" section    

biz_stories = client.top_stories(section="business")
(len(biz_stories))

## Return the first story, its type (it's a dict), and its keys

story = biz_stories[0]
pprint(type(story))
pprint(story.keys())
#pprint(story)

## Return the title, abstract, des_facet, and org_facet
pprint(story["title"])
pprint(story["abstract"])
pprint(story["des_facet"])
pprint(story["org_facet"])

## Return the titles of articles that have the word "crypto" in their
## ...title, abstract, des_facet, or org_facet
search_phrase = "crypto"

crypto_stories = []

    