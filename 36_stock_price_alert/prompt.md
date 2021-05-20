# Day 36 : Stock Price Alert

Create an app that checks selected stock price and when the closing price changes more than 5 %, send you a text alert with related news article.

## My Solution

https://github.com/satomiichii/python_entry/blob/master/36_stock_price_alert/main.py

## Today's Takeaway

- Stock API > https://www.alphavantage.co/
- News API > https://newsapi.org/
- The API endpoint for querying with params is 'END_POINT_URL/query' otherwise it will just return root html not json
- datetime module hint
```buildoutcfg
# get today's date in 'YYYY-MM-DD' format
today = datetime.date.today
# get yesterday's date with timedelta method. days attribute is num of day to calculate difference in date
yesterday = today - datetime.timedelta(days=1)
```
