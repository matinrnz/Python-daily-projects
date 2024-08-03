import requests
import os
from telegram import Update
from telegram.ext import *

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = os.environ.get("STOCK_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")
TOKEN = os.environ.get("TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME")


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then send the articles.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
# print(response.json())
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# 1- Get yesterday's closing stock price.
yesterday_data = data_list[0]
yesterday_price = float(yesterday_data["4. close"])
# 2- Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_price = float(day_before_yesterday_data["4. close"])

# 3- Find the positive difference between 1 and 2.
difference = yesterday_price - day_before_yesterday_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# 4- Work out the percentage difference in price between closing price yesterday and closing price the day
# before yesterday.
diff_percentage = round((difference / day_before_yesterday_price) * 100)
# 5- If percentage is greater than 5 then send the articles.
if abs(diff_percentage) > 5:
    # print("Get News")
    # STEP 2: https://newsapi.org/
    # 6- Use the News API to get articles related to the COMPANY_NAME.
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
    # 8- Create a new list of the first 3 articles' headline and description.
    formatted_articles = [(f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \n"
                           f"Brief: {article['description']}") for article in three_articles]

    # formatted_articles = ["article1", "article2", "article3"]
    # 9- Send each article as a separate message via Telegram.
    async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hello! I send you 3 daily stock articles.")


    async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        for article in formatted_articles:
            await update.message.reply_text(article)


    async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f"Update: {update} caused error {context.error}")


    if __name__ == '__main__':
        print('Starting bot...')
        app = Application.builder().token(TOKEN).build()

        # Commands
        app.add_handler(CommandHandler('start', start_command))
        app.add_handler(CommandHandler('news', news_command))

        # Errors
        app.add_error_handler(error)

        # Polls the bot
        print('Polling...')
        app.run_polling(poll_interval=3)
