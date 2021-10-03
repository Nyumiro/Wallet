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


def currency_converter(delta_balance, sender, receptionist):
    currencies_collection = {'RUB/EUR': (lambda exchange_rates=82: delta_balance * exchange_rates)(),
                             'RUB/USD': (lambda exchange_rates=72: delta_balance * exchange_rates)(),
                             'EUR/RUB': (lambda exchange_rates=82: delta_balance / exchange_rates)(),
                             'EUR/USD': (lambda exchange_rates=1.16: delta_balance / exchange_rates)(),
                             'USD/RUB': (lambda exchange_rates=72: delta_balance / exchange_rates)(),
                             'USD/EUR': (lambda exchange_rates=1.16: delta_balance * exchange_rates)()}

    return delta_balance if sender.currency == receptionist.currency else currencies_collection[sender.currency+'/'+receptionist.currency]

