## Testing cryptotrends.py

import os
import pytest #> I could not get pytest to work even though it's installed in this environment

from dotenv.main import load_dotenv
load_dotenv()


## define and test for certain variable values and/or formatting below

from app.cryptotrends import print_articles
def test_print_articles():
    assert print_articles(BTC_frq > 0) == print("Latest: ",btc_articles[0]["headline"]["main"])
    assert print_articles(ada_frq > 0) == print("Latest: ",ada_articles[0]["headline"]["main"])
    assert print_articles(doge_frq > 0) == print("Latest: ",doge_articles[0]["headline"]["main"])
    assert print_articles(eth_frq > 0) == print("Latest: ",eth_articles[0]["headline"]["main"])
    assert print_articles(xrp_frq > 0) == print("Latest: ",xrp_articles[0]["headline"]["main"])
