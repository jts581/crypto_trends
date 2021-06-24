import requests
import os
from dotenv import load_dotenv

# retrieve API Key from env file
load_dotenv()

NYT_API_KEY = os.getenv("NYT_API_KEY")



filter_query = input("Please enter a cryptocurrency from this list: Bitcoin, Etherium, Dogecoin, Cardano, Ripple -- ")

# Article Search API
request_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=cryptocurrency&fq={filter_query}&api-key={NYT_API_KEY}"

