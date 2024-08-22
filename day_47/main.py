import requests
from bs4 import BeautifulSoup
import smtplib
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Email information
my_email = getenv('EMAIL')
password = getenv('APP_PASSWORD')  # app password

# retrieving data
amazon_response = requests.get('https://www.amazon.com/MSI-RTX-4060-Architecture-2X/dp/B0C8BPW1SP/ref=sr_1_3')
amazon_item_website = amazon_response.text
soup = BeautifulSoup(amazon_item_website, 'html.parser')
item_price = soup.select_one('.a-price-whole')
fraction = soup.select_one('.a-price-fraction')
full_item_price = float(item_price.get_text() + fraction.get_text())
default_price = 294.76  # original price of item


# if price drops
if full_item_price < default_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secures connection by making the email encrypted
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="recipient email here",
                            msg=f"Subject: Amazon Item Price Drop\n\n "
                                f"MSI Gaming GeForce RTX 4060 8GB GDRR6 128-Bit HDMI/DP Nvlink TORX Fan 4.0 Ada Lovelace"
                                f" Architecture Graphics Card (RTX 4060 Ventus 2X Black 8G OC) is now ${full_item_price}!")
