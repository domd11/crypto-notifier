import requests
import tkinter as tk
from datetime import datetime
import smtplib

username = "dominiquedesertb@gmail.com"
pwd = "obzxjqoojxnkqjyb"

url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
response = requests.get(url).json()
price = response["USD"]

if price > 1100:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(username, pwd)

        subject = 'Ethereum Above 200 - Sell'
        body = 'Ethereum is above 2000'

        msg = f'Subject:{subject}\n\n{body}'
        smtp.sendmail(username, username, msg); 

        print("Sell Ethereum!")

if price < 900:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(username, pwd)

        subject = 'Ethereum Below 1200 - Buy'
        body = f'Ethereum is below 1200\n\nCurrent Price: ${price}'

        msg = f'Subject:{subject}\n\n{body}'
        smtp.sendmail(username, username, msg); 

        print("Buy Ethereum!")


time = datetime.now().strftime("%H:%M:%S")




