import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.jumia.co.ke/ultrabooks/"

response = requests.get(base_url)

products_list = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.select(".core")
    for card in cards:
        title = card.select_one(".name").text
        price = card.select_one(".prc").text
        product_details = {
            "Title" : title,
            "Price" : price.replace("KSh",""),
            "Source_URL" :base_url
        }
        products_list.append(product_details)

print(products_list)