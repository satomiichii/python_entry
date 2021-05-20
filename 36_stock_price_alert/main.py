import os
import requests
import datetime as dt
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc."
DATA_TYPE = 'TIME_SERIES_DAILY_ADJUSTED'

# fetch today's date
YESTERDAY = str(dt.date.today() - dt.timedelta(days=1))
DAY_BEFORE = str(dt.date.today() - dt.timedelta(days=2))

# store rate_change for later use

rate_change = 0

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

params = {
    'function': DATA_TYPE,
    'symbol': STOCK,
    'apikey': os.environ['API_KEY_STOCK']
}

response_stock = requests.get('https://www.alphavantage.co/query', params=params)
response_stock.raise_for_status()
stock_data = response_stock.json()
daily_data = stock_data['Time Series (Daily)']

# function to check price change between yesterday and day before


def check_price():
    global rate_change
    yesterday_price = float(daily_data[YESTERDAY]['4. close'])
    day_before_price = float(daily_data[DAY_BEFORE]['4. close'])
    rate_change = (yesterday_price/day_before_price * 100) - 100
    print(rate_change)
    if rate_change > 5 or rate_change < -5:
        return True
    else:
        return True


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_params = {
    'apiKey': os.environ['API_KEY_NEWS'],
    'q': COMPANY_NAME
}


def get_news():
    response_news = requests.get('https://newsapi.org/v2/everything', params=news_params)
    response_news.raise_for_status()
    news_data = response_news.json()['articles']
    return news_data[2]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

if check_price():
    rate_change = round(rate_change, 2)
    emoji = '🔺'
    if rate_change < 0:
        emoji = '🔻'
    news = get_news()
    message = client.messages \
                    .create(
                         body=f"{COMPANY_NAME}: {emoji}{rate_change}\n"
                              f"HeadLine: {news['title']}\n"
                              f"Brief: {news['description']}",
                         from_=os.environ['SENDER_NUMBER'],
                         to=os.environ['TO_NUMBER']
                     )


# Optional: Format the SMS message like this:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""
