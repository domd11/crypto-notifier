import requests
import tkinter as tk
from datetime import datetime
from twilio.rest import Client 
import keys
import schedule
import time


def notify_sol():
    username = "dominiquedesertb@gmail.com"
    pwd = "obzxjqoojxnkqjyb"

    url = "https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD"
    response = requests.get(url).json()
    price = response["USD"]

    if price > 80:
        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
            body = f'Solana price is above $80 - Sell Solana - Current Price: ${price}', 
            from_=keys.twilio_number,
            to=keys.target_person
        )
        print(f'Price is greater than 80, sell. Price - ${price}')
    
    elif price < 50:
        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
            body = f'Solana price is less than $40 - Buy solana - Current Price: ${price}', 
            from_=keys.twilio_number,
            to=keys.target_person
        )
        print(f'Solana is less than 40 - Buy solana - Price: ${price}')
    
    else:
        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
            body = f'Solana price is ${price}', 
            from_=keys.twilio_number,
            to=keys.target_person
        )
        print(f'Current solana price: ${price}')

notify_sol()
schedule.every(1).hour.do(notify_sol)

while True:
    schedule.run_pending()
    time.sleep(1)