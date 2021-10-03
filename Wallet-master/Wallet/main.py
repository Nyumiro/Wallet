from time import *
from classes import *
from functions import *
from csv_reader import *
from datetime import datetime

wallets = read_wallets()  # считываем созданные кошельки из файла wallets.csv
history = read_history()  # считываем историю из файла history.csv

while True:
    print('Введите команду. Введите HELP для вывода всех команд. Для завершения работы программы введите команду EXIT.')

    command = input()

    if command == 'HELP':
        print('CREATE -- После ввода данной команды открывается возможность создания нового счёта.\n'
              'BLOCK_WALLET -- Данная операция позволяет изменить состояние существующего счёта. \n'
              'SHOW-WALLET -- Данная команда показывает всю информацию о существующем счёте.\n'
              'SHOW_ALL_WALLETS -- Данная команда выводит все созданные счета. \n'
              'MONEY_OUT -- Данная команда позволяет вывести деньги с существующего счёта. \n'
              'MONEY_ADD -- Данная команда позволяет пополнить существующий счет на указанную сумму. \n'
              'TRANSACT -- Данная команда позволяет переводить деньги между существующими счетами. '
              'Если кошельки используют разные валюты, то сумма, введенная отправителем, конвертируется в валюту получателя.\n'
              'SHOW_ALL_HISTORY -- Данная команда показывает всю историю операций.\n\n'
              'EXIT -- Данная команда завершает работу программы.')
        continue

    if command == 'CREATE':
        print('Запущена программа создания кошелька.')
        owner_name = input('Введите имя владельца кошелька: ')
        owner_lastname = input('Введите фамилию владельца кошелька: ')
        owner_patronymic = input('Введите отчество владельца кошелька: ')
        owner_city = input('Введите город проживания: ')
        print('Введите используемую валюту. (Поддерживаемые валюты: RUB EUR USD)')
        currency = currency_validation()
        owner_id = id_generator(wallets)
        wallets[owner_id] = Wallet(owner_id, owner_name, owner_lastname, owner_patronymic, owner_city, 0, currency, False)
        print(f'Кошелек создан. Кошельку присвоен номер: {owner_id} \n\n')
        continue

    if command == 'BLOCK_WALLET':
        id = int(input('Введена команда блокировки/разблокировки кошелька. Введите номер счёта: '))
        if id not in wallets.keys():
            print('Недопустимая операция. Указанный кошелек не найден.\n\n')
            continue
        wallet = wallets[id]
        wallet.is_blocked = False if wallet.is_blocked else True
        print(f'Операция выполнена успешно. '
              f'Состояние номера счета {wallet.owner_id}: {"заблокирован" if wallet.is_blocked else "разблокирован"}.\n\n')
        continue

    if command == 'SHOW_WALLET':
        id = int(input('Запущена программа вывода информации о кошельке. Введите номер кошелька: '))
        if id not in wallets.keys():
            print('Недопустимая операция. Указанный кошелёк не найден.\n\n')
            continue
        wallet = wallets[id]
        wallet.show_info()
        continue

    if command == 'SHOW_ALL_WALLETS':
        print('Запущена программа, показывающая все созданные кошельки.\n\n')
        for wallet in wallets:
            wallets[wallet].show_info()
        continue

    if command == 'MONEY_OUT':
        id = int(input('Запущена программа вывода денег. Введите номер счета: '))
        if id not in wallets.keys():
            print('Недопустимая операция. Указанный кошелёк не найден.\n\n')
            continue
        wallet = wallets[id]
        if wallet.is_blocked:
            print('Недопустимая операция. Счет заблокирован.\n\n')
            continue
        print('Введите сумму: ')
        delta_balance = delta_balance_validation()
        if wallet.balance < delta_balance:
            print('Недопустимая операция. Недостаточно средств на счете.\n\n')
            continue
        wallet.balance -= delta_balance
        history.append(HistoryItem(wallet.owner_id, command, delta_balance,
                                   wallet.currency, -1, wallet.balance, str(datetime.now())))
        print(f'Успешно. Баланс счета {wallet.owner_id} изменен. \n'
              f'Произошло списание средств на сумму {delta_balance} {wallet.currency}. \n'
              f'Текущий баланс счета: {wallet.balance} {wallet.currency}.\n\n')
        continue

    if command == 'MONEY_ADD':
        id = int(input('Запущена программа пополнения средств. Введите номер кошелька: '))
        if id not in wallets.keys():
            print('Недопустимая операция. Указанный кошелёк не найден.\n\n')
            continue
        wallet = wallets[id]
        if wallet.is_blocked:
            print('Недопустимая операция. Указанный кошелёк заблокирован.\n\n')
            continue
        print('Введите сумму: ')
        delta_balance = delta_balance_validation()
        wallet.balance += delta_balance
        history.append(HistoryItem(wallet.owner_id, command, delta_balance,
                                   wallet.currency, -1, wallet.balance, str(datetime.now())))
        print(f'Успешно. Баланс счета {wallet.owner_id} изменен. \n'
              f'Произошло пополнение средств на сумму {delta_balance} {wallet.currency}. \n'
              f'Текущий баланс счета: {wallet.balance} {wallet.currency}.\n\n')
        continue

    if command == 'TRANSACT':
        id_sender = int(input('Введена команда перевода между кошельками. Введите номер кошелька отправителя: '))
        if id_sender not in wallets.keys():
            print('Недопустимая операция. Кошелёк отправителя не найден.\n\n')
            continue
        wallet_sender = wallets[id_sender]
        if wallet_sender.is_blocked:
            print('Недопустимая операция. Кошелёк отправителя заблокирован.\n\n')
            continue
        id_recipient = int(input('Введите номер счёта получателя: '))
        if id_recipient not in wallets.keys() and id_recipient == id_sender:
            print('Недопустимая операция. Счет получателя не найден или равен счету отправителя.')
            continue
        wallet_recipient = wallets[id_recipient]
        if wallet_recipient.is_blocked:
            print('Недопустимая операция. Счет получателя заблокирован.\n\n')
            continue
        print(f'Кошелек отправителя использует валюту {wallet_sender.currency}. '
              f'Кошелек получателя использует валюту {wallet_recipient.currency}.')
        print(f'Введите сумму перевода в {wallet_sender.currency}: ')
        delta_balance = delta_balance_validation()
        if delta_balance > wallet_sender.balance:
            print('Недопустимая операция. Недостаточно средств на кошельке отправителя.')
            continue
        diff_delta_balance = currency_converter(delta_balance, wallet_sender, wallet_recipient)
        wallet_recipient.balance += diff_delta_balance
        wallet_sender.balance -= delta_balance
        print(f'Успешно. \n'
              f'Произошел перевод средств на сумму {diff_delta_balance} {wallet_recipient.currency} '
              f'со счёта {wallet_sender.owner_id} на счёт {wallet_recipient.owner_id}. \n'
              f'Текущий баланс счета отправителя: {wallet_sender.balance} {wallet_sender.currency} \n'
              f'Текущий баланс счета получателя: {wallet_recipient.balance} {wallet_recipient.currency}.')
        history.append(HistoryItem(wallet_sender.owner_id, command, -delta_balance, wallet_sender.currency,
                                   wallet_recipient.owner_id, wallet_sender.balance, str(datetime.now())))
        history.append(HistoryItem(wallet_recipient.owner_id, command, diff_delta_balance, wallet_recipient.currency,
                                   wallet_sender.owner_id, wallet_recipient.balance, str(datetime.now())))
        continue

    if command == 'SHOW_HISTORY':
        for i in range(len(history)):
            print(f'Операция: {i+1} {history[i].owner_id, history[i].type_of_operation, history[i].delta_balance, history[i].currency, history[i].recipient_id, history[i].owner_new_balance, history[i].datetime}. \n')
        continue

    if command == 'EXIT':
        print('Завершение работы.')
        write_wallets(wallets)
        write_history(history)
        break

    else:
        print('Неизвестная команда.')
        continue
