from datetime import datetime

from kurs3_.funct import get_data, sort_data, filename, filter_data, check_data, data_format
from tests.conftest import test_data

filename1 = ''

def test_get_data():
    assert get_data(filename) != []
    assert get_data('') == 'Файл с операциями "operations.json" отстутствует'


def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    for v in test_data:
        print(v['date'])
    assert [x['date'] for x in sorted_data] == ['2019-07-03T18:35:29.512364', '2019-03-23T10:45:06.972075',\
                                                '2018-06-30T02:08:58.425572', '2017-08-26T10:50:58.294041']


def test_filter_data(test_data):
    assert filter_data(test_data) == [
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2019-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }
        ]


def test_check_data(test_data):
    fail_data = 0
    tested_data = check_data(test_data)
    for transaction in test_data:
        if ('id' or 'state' or 'id' or 'operationAmount' or 'description' or 'from') not in transaction:
            fail_data += 1
    assert fail_data == 0
    # assert tested_data == 'Все данные транзакций в файле корректны'


def test_data_format(test_data):
    format_data = data_format(test_data)


    print (format_data[0])
    assert format_data[0] == """
26.08.2017 Перевод организации
Maestro 1596 83** ****5199 -> Счет  **9589
31957.58 руб.
        """



