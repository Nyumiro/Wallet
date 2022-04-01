# Wallet
Первое задание семинара по дисциплине Алгоритмы и структуры данных на языке Python. Реализация простого кошелька.

Задача “Кошелек Часть-1”

Создать программу для работы с деньгами пользователей.

Программа должна позволять:
6. Создавать кошельки пользователей для хранения денег
7. Пополнять кошельки
8. Снимать деньги с кошелька
9. Проверка баланса кошелька
10. Переводить сумму на другой кошелек

О каждом кошельке храним:
- owner_name - Имя владельца
- balance - баланс кошелька
- currency - валюта

Пункт “Создание нового кошелька” -
Создается кошелек с нулевым балансом. Обязательно указание Имени владельца и валюты.

Пункт “Пополнение кошелька” -
Добавляет указанную сумму к балансу кошелька.

Пункт “Снятие денег” -
Уменьшает баланс на указанную сумму.
Нельзя снять больше денег, чем есть на балансе.

Пункт “Проверка баланса кошелька” - 
Выводит информацию о состоянии баланса и имени владельца и валюте.

Пункт “Перевод на другой кошелек” - 
Переводит указанную сумму на указанный кошелек.
Нельзя перевести сумму больше, чем есть на балансе.

Задача “Кошелек Часть-2”
Доработать программу "Кошелек Часть-1".
Доработки:
1. Хранить больше информации о владельце: Фамилия, Отчество, город
проживания
i. Проверка баланса также должна отображать и Фамилию владельца
2. Сохранять всю историю операций с кошельком: пополнение, снятие,
переводы.
3. Отображает всю историю операций
i. Отображать историю только заданных операций
4. Блокировать/разблокировать кошелек. С заблокированным кошельком
доступна только операция Проверка баланса". Прочие операции должны
сообщать, что кошелек заблокирован.