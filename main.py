import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "Your_stock_endpoint"
NEWS_ENDPOINT = "Your_news_endpoint"

STOCK_API_KEY = "Your_stock_api_key"
NEWS_API_KEY = "Your_news_api_key"
account_sid = "Your_account_sid_number"
auth_token = "Your_auth_token"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)
diff_percent = difference / float(yesterday_closing_price) * 100
print(diff_percent)

if diff_percent > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in
                            three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="Your_twilio_number",
            to="Your_mobile_number"
        )
     

