from random import random


def id_generator(wallets):
    while True:
        id = int(random() * 100)
        if not (id in wallets):
            return id


def currency_validation():
    currency = input()
    if currency not in ('RUB', 'EUR', 'USD'):
        print('Валюта не определена. Пожалуйста, введите один из вариантов: RUB, EUR, USD.')
        return currency_validation()
    return currency


def delta_balance_validation():
    delta_balance = input()
    try:
        return int(delta_balance) if int(delta_balance) > 0 else delta_balance_validation()
    except Exception:
        print('Недопустимый ввод. Пожалуйста, введите сумму, используя цифры.')
        return delta_balance_validation()


currencies_collection = {'RUB/EUR': 1 / 82,
                         'RUB/USD': 72,
                         'EUR/RUB': 82,
                         'EUR/USD': 1.16,
                         'USD/RUB': 1 / 72,
                         'USD/EUR': 1 / 1.16}


def currency_converter(delta_balance, sender, receptionist):
    diff_delta_balance = (lambda rate: delta_balance * rate)
    return delta_balance if sender.currency == receptionist.currency else diff_delta_balance(
        currencies_collection[sender.currency + '/' + receptionist.currency])
