class HistoryItem:
    def __init__(self, owner_id, type_of_operation, delta_balance, currency, recipient_id, owner_new_balance):
        self.owner_id = owner_id
        self.type_of_operation = type_of_operation
        self.delta_balance = delta_balance
        self.currency = currency
        self.recipient_id = recipient_id
        self.owner_new_balance = owner_new_balance


class Wallet:
    def __init__(self, owner_id, owner_lastname,owner_name, owner_patronymic, owner_city, balance, currency, is_blocked):
        self.owner_id = owner_id
        self.owner_lastname = owner_lastname
        self.owner_name = owner_name
        self.owner_patronymic = owner_patronymic
        self.owner_city = owner_city
        self.balance = balance
        self.currency = currency
        self.is_blocked = is_blocked

    def show_info(self):
        print(f'Номер счета: {self.owner_id}. \n'
              f'ФИО владельца: {self.owner_name} {self.owner_lastname} {self.owner_patronymic}. \n'
              f'Город проживания: {self.owner_city}. \n'
              f'Баланс: {self.balance} {self.currency}. \n'
              f"Состояние: {'заблокирован' if self.is_blocked else 'разблокирован'}.\n\n")

