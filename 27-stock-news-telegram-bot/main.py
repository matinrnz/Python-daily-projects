import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = os.environ.get("STOCK_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
data_list = [value for (key,value) in data.items()]
# print(data_list)
# 1- Get yesterday's closing stock price.
yesterday_data = data_list[0]
yesterday_price = float(yesterday_data["4. close"])
# 2- Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_price = float(yesterday_data["4. close"])
# 3- Find the positive difference between 1 and 2.
difference = abs(yesterday_price - day_before_yesterday_price)
# print(difference)
# 4- Work out the percentage difference in price between closing price yesterday and closing price the day
# before yesterday.
diff_percentage = (difference / day_before_yesterday_price) * 100
# 5- If percentage is greater than 5 then print("Get News").
if diff_percentage > 5:
    # print("Get News")
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # 6- Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # print(articles)
    # 7- Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]
    print(three_articles)

    # STEP 3: Use telegram bot api
    # to send a separate message with each article's title and description.

# 8- Create a new list of the first 3 article's headline and description using list comprehension.

# 9- Send each article as a separate message via Telegram.

# Optional: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

