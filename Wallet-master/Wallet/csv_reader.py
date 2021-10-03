from classes import *
import csv


def wallet_to_array(wallet):
    return [wallet.owner_id, wallet.owner_lastname, wallet.owner_name, wallet.owner_patronymic, wallet.owner_city,
            wallet.balance, wallet.currency, wallet.is_blocked]


def history_to_array(history):
    return [history.owner_id, history.type_of_operation, history.delta_balance, history.currency,
            history.recipient_id, history.owner_new_balance, history.datetime]


def array_to_wallet(array):
    return Wallet(int(array[0]), array[1], array[2], array[3], array[4], int(array[5]), array[6], array[7] == 'True')


def array_to_history(array):
    return HistoryItem(int(array[0]), array[1], int(array[2]), array[3], int(array[4]), int(array[5]), array[6])


def write_wallets(wallets):
    wallets_list = []
    for value in wallets.values():
        wallets_list.append(wallet_to_array(value))
    file = open('wallets.csv', 'w', newline='\n', encoding="utf-8")
    with file:
        writer = csv.writer(file)
        writer.writerows(wallets_list)


def read_wallets():
    wallets = dict()
    file = open('wallets.csv', 'r', encoding="utf-8")
    with file:
        reader = csv.reader(file)
        for row in reader:
            wallet = array_to_wallet(row)
            wallets[wallet.owner_id] = wallet
    return wallets


def write_history(history):
    history_ = []
    for value in history:
        history_.append(history_to_array(value))
    file = open('history.csv', 'w', newline='\n', encoding="utf-8")
    with file:
        writer = csv.writer(file)
        writer.writerows(history_)


def read_history():
    history = list()
    file = open('history.csv', 'r', encoding="utf-8")
    with file:
        reader = csv.reader(file)
        for row in reader:
            history_item = array_to_history(row)
            history.append(history_item)
    return history
