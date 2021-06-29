# Trending Cryptocurrencies App (Python)

Rank a set of cryptocurrencies by the number of times they are mentioned in NY Times Top Stories. 

## Installation

Fork [this repo] (https://github.com/jts581/crypto_trends), then clone or download the forked repo onto your local computer (for example to the Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/crypto-trends-py/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "cryptotrends-env":

```sh
conda create -n cryptotrends-env python=3.8
conda activate cryptotrends-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Resources

This app uses the NY Times 'Article Search' API
More information here: https://developer.nytimes.com/docs/articlesearch-product/1/overview 

## Configuration
Enter functional... 
- NYT API Key as NYT_API_KEY
- Sendgrid API Key as SENDGRID_API_KEY
- Sendgrid Sender address as SENDER_ADDRESS"
- Sendgrid Template ID as SENDGRID_TEMPLATE_ID

in the dotenv file

## Usage
Running the report:

Enter the below code in terminal:
```sh
python app/cryptotrends.py
```

User enters the number of historical days of activity they want to view

## Testing

Running tests:

```sh
pytest
```
## Codeclimate results

https://codeclimate.com/github/LLC314/freestyle_project/issues

