import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.jumia.co.ke/ultrabooks/"

def currency_convertor(amount,base_currency,target_currency):
    api_key = "6b286fed0ca4b25d316d8582"
    api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}/{amount}"
    api_response = requests.get(api_url)
    data = api_response.json()
    if data["result"] == "success":
        return data["conversion_result"]
    else:
        print("unable to do the conversion! Please check your Url")
        return None


response = requests.get(base_url)

products_list = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.select(".core")
    for card in cards:
        title = card.select_one(".name").text
        price = card.select_one(".prc").text.replace("KSh","").replace(",","")
        price_in_usd = currency_convertor(int(price),"KES","USD")
        product_details = {
            "Title" : title,
            "Price" : price,
            "USD_Price" : price_in_usd ,
            "Source_URL" :base_url
        }
        products_list.append(product_details)

