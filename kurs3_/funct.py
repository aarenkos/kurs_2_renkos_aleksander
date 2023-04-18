import json
import os
from datetime import datetime

filename = 'operations.json'


def get_data(filename):
    """Функция загружает данные из файла operations.json"""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    else:
        return 'Файл с операциями "operations.json" отстутствует'


def check_data(data):
    """Проверка все ли данные транзакций в файле корректны\n
    Возвращает отчет о корректности транзакций"""
    fail_data = 0
    for transaction in data:
        if ('id', 'state', 'id', 'operationAmount', 'description', 'from') not in transaction:
            fail_data += 1
            return print(f'В файле есть не корректные данные транзакций. Колличество - {fail_data} ')
    return print('Все данные транзакций в файле корректны')


def filter_data(data):
    """Функция фильтрует транзакции по статусу EXECUTED\n
    Возвращает отфильтрованные данные"""
    data = [inf for inf in data if 'state' in inf and inf['state'] == 'EXECUTED']
    return data


def sort_data(data):
    """Функция сортирует транзакции по дате. Возвращает 5 самых новых"""
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def data_format(data):
    """Функция подготавливает данные в требуемом формате и возвращает их"""

    formatted_data = []
    # Запуск цикла отдельно по каждой транзакции
    for transaction in data:

        # Перевод даты в формат ДД.ММ.ГГГГ, запись в переменную date
        date = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

        # Запись в переменную description  описание типа перевода
        description = transaction['description']

        # Переменная для указания направления перевода
        from_arrow = '->'

        # Создание переменных с номером счета/карты откуда перевод
        if 'from' in transaction:
            sender = transaction['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** ****{sender_bill[-4:]}"
        else:
            sender_info = ""
            sender_bill = ""
            from_arrow = ""

        # Создание переменных с номером счета/карты куда перевод
        if 'to' in transaction:
            received = transaction['to'].split()
            received_bill = received.pop(-1)
            received_info = " ".join(received)
            received_bill = f"**{received_bill[-4:]}"
        else:
            received_info = ""
            received_bill = ""
        # Создание переменных с суммой перевода и валютой перевода
        money_information = transaction['operationAmount']
        amount_money = money_information['amount']
        currency_money = money_information['currency']

        # Добавление переменных в список по каждой транзакции
        if sender_bill != '':
            formatted_data.append(f'''
{date} {description}
{sender_info} {sender_bill} {from_arrow} {received_info}  {received_bill}
{amount_money} {currency_money['name']}
        ''')
        else:
            formatted_data.append(f'''
{date} {description}
{received_info}  {received_bill}
{amount_money} {currency_money['name']}
        ''')
    return formatted_data
