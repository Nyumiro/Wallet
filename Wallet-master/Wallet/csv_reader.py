from classes import *
import csv


def wallet_to_array(wallet):
    return [wallet.owner_id, wallet.owner_lastname, wallet.owner_name, wallet.owner_patronymic, wallet.owner_city,
            wallet.balance, wallet.currency, wallet.is_blocked]


def array_to_wallet(array):
    return Wallet(int(array[0]), array[1], array[2], array[3], array[4], int(array[5]), array[6], array[7] == 'True')


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
    file_2 = open('wallets.csv', 'r', encoding="utf-8")
    with file_2:
        reader = csv.reader(file_2)
        for row in reader:
            wallet = array_to_wallet(row)
            wallets[wallet.owner_id] = wallet
    return wallets
