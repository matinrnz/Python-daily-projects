import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os


ACCEPT_LANGUAGE = os.environ.get("ACCEPT_LANGUAGE")
USER_AGENT = os.environ.get("USER_AGENT")
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
BUY_PRICE = 100

headers = {'Accept-Language': ACCEPT_LANGUAGE,
           'User-Agent': USER_AGENT}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
# print(price_as_float)
product_title = soup.find(id="productTitle").getText().strip()
# print(product_title)
message = f"{product_title} is now {price_as_float}\n{URL}"
# print(message)

if price_as_float < BUY_PRICE:
    # print("Buy")
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Amazon Price Alert!\n\n{message}".encode("utf-8")
            )
            print("Sent")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
