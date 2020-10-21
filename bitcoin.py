import json
import requests


url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    coins_get = get_coins()
    bitcoin = convert_bitcoins_to_dollars(coins_get)
    display_results(coins_get, bitcoin)


def get_coins():# getting the number of coins greater or equal to 0
    try:
        dollar_value = float(input('Enter the coins:only number '))
        if dollar_value >= 0:
            return dollar_value
        else:
            print('Enter a number greater than 0')
    except ValueError:
        print('Enter a valid number.')

def exchange_rate(rate):# getting data from Api
    try:
        response = requests.get(url)
        data = response.json()
        dollars_exchange_rate = data['bpi']['USD']['rate_float']
        return(dollars_exchange_rate)
    except Exception as e:
        print('Error occured',e)


def get_convert_rate(coins, bitcoin_rate):
    return coins * bitcoin_rate

def convert_bitcoins_to_dollars(coins):#convert coins into  dollars
    try:

        rate_of_exchange = exchange_rate(coins)
        bitcoin = get_convert_rate(coins, rate_of_exchange)
        return bitcoin
    except Exception as e:
        print('Error occured',e)
 

def display_results(coins, bitcoin_rate):#printing the result
    try:

        print(f'{coins} coins is equal to ${bitcoin_rate:.2f}')
    except Exception as e:
        print('Error occured',e)




if __name__ == '__main__':
    main()
