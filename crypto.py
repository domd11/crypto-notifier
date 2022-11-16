import requests
import tkinter as tk
from datetime import datetime
from twilio.rest import Client 
import keys
import schedule
import time

print("Running Code..")
def notify_eth():
    username = "_____________"
    pwd = "__________________"

    url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
    response = requests.get(url).json()
    price = response["USD"]
        

    if price > 1100:  
        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
        body = f'Ethereum price is above $1100 - ${price}',
        from_=keys.twilio_number, 
        to=keys.target_person)

        print("Sell Ethereum!")

    elif price < 900:
        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
        body = f'Ethereum price is above $1100 - Current Price: ${price}', 
        from_=keys.twilio_number,
        to=keys.target_person)

        print("Buy Ethereum")
        
    else:
        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
        body = f'Ethereum price is ${price}', 
        from_=keys.twilio_number,
        to=keys.target_person)

        print(f'The current price of ethereum is  - ${price}')

def notify_sol():
    username = "_________________________"
    pwd = "_________________"

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

notify_eth()
notify_sol()
schedule.every(1).hour.do(notify_eth)
schedule.every(1).hour.do(notify_sol)

while True:
    schedule.run_pending()
    time.sleep(1)
