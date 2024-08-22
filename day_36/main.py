import smtplib
import requests
from newsapi import NewsApiClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# STOCK COMPANY
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STOCK API ENDPOINT/KEY/INFO
STOCK_ENDPOINT = getenv('STOCK_ENDPOINT')
print(STOCK_ENDPOINT)
STOCK_API_KEY = getenv('STOCK_API_KEY')
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

# NEWS API ENDPOINT/KEY/INFO
NEWS_ENDPOINT = getenv('NEWS_ENDPOINT')
print(NEWS_ENDPOINT)
NEWS_API_KEY = getenv('NEWS_API_KEY')
NEWS_API_CLIENT = NewsApiClient(api_key=NEWS_API_KEY)
EVERY_ARTICLE = NEWS_API_CLIENT.get_everything(q=COMPANY_NAME,
                                               from_param='2024-02-28',
                                               to='2024-02-27',
                                               )

# EMAIL INFO
EMAIL_SENDER = getenv('EMAIL_SENDER')
APP_PASSWORD = getenv('APP_PASSWORD')
EMAIL_RECIPIENT = getenv('EMAIL_RECIPIENT')

# yesterday and the day before yesterday's stock data
stock_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
stock_data = stock_response.json()['Time Series (Daily)']
stock_list = [value for (date, value) in stock_data.items()]
yesterday_closing_price_data = stock_list[1]['4. close']
day_before_yesterday_closing_price_data = stock_list[2]['4. close']

# Finds the positive difference and create emote to refer that stock has lowered for risen
difference = float(yesterday_closing_price_data) - float(day_before_yesterday_closing_price_data)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# percentage create the percentage
diff_percent = round((difference / float(yesterday_closing_price_data)) * 100)


# Sends the last 3 news about the company
if abs(diff_percent) < 4:
    three_recent_articles = EVERY_ARTICLE['articles'][:3]
    articles_titles = [dictionary['title'] for dictionary in three_recent_articles]
    articles_descriptions = [dictionary['description'] for dictionary in three_recent_articles]
    articles_urls = [dictionary['url'] for dictionary in three_recent_articles]
    article_one = f"Title:\n{articles_titles[0]}\nBrief:\n{articles_descriptions[0]}"
    article_two = f"Title:\n{articles_titles[1]}\nBrief:\n{articles_descriptions[1]}"
    article_three = f"Title:\n{articles_titles[2]}\nBrief:\n{articles_descriptions[2]}"
    print(article_one)
    print(article_two)
    print(article_three)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secures connection by making the email encrypted
        connection.login(user=EMAIL_SENDER, password=APP_PASSWORD)
        connection.sendmail(from_addr=EMAIL_SENDER, to_addrs=EMAIL_RECIPIENT,
                            msg=f"Subject:STOCKS CHANGE\n\n {up_down}{diff_percent}%\n"
                                f"Article 1\n{article_one}\n"
                                f"Article 2\n{article_two}\n"
                                f"Article 3\n{article_three}")

