# write your code here!
import sys
import requests


def cash(coin_have_cal):
    main_cash = {}    # вызов данных с сайта по волюте
    for key in coin_have_cal:
        coins = coin_have_cal[key]["code"]
        rate = coin_have_cal[key]["rate"]
        if coins == "USD":
            money_cash = {coins: rate}
            main_cash.update(money_cash)    # создание словаря для валюты (валюта: курс)
        elif coins == "EUR":
            money_cash = {coins: rate}
            main_cash.update(money_cash)
        else:
            pass
    return main_cash


a = input()
coin_have = requests.get(f"http://www.floatrates.com/daily/{a.lower()}.json").json()
cash = cash(coin_have)
while True:
    for line in iter(input, ""):
        amount_money = float(input())
        currency_want = line.upper()
        if currency_want in cash.keys():
            calculation = round(amount_money * float(cash[currency_want]), 2)
            print(f"Checking the cache...\nOh! It is in the cache!\nYou received {calculation} {currency_want}.")
        else:
            coin_search = requests.get(f"http://www.floatrates.com/daily/{a.lower()}.json").json()
            for search in coin_search:
                search_coins = coin_search[search]["code"]
                if search_coins == currency_want:
                    search_rate = coin_search[search]["rate"]
                    calculation = round(amount_money * float(search_rate), 2)
                    print(f"Checking the cache...\nSorry, but it is not in the cache!\nYou received {calculation} {currency_want}.")
                    info = {search_coins: search_rate}
                    cash.update(info)
    else:
        break
