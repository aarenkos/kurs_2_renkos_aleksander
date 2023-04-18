import time

from funct import get_data, check_data, filter_data, sort_data, data_format, filename


def main():
    """Функция, которая выводит на экран список из 5 последних выполненных клиентом операций,
    операции берутся из файла operations.json"""
    # Загрузка данных из файла.Проверка, есть ли такой файл.
    data = get_data(filename)
    if data == 'Файл с операциями "operations.json" отстутствует':
        return print(data)
    else:
        print('Данные получены')
    time.sleep(2)

    # Проверка транзакций в файле, все ли строки данных транзакции есть.
    check_data(data)
    time.sleep(2)

    # Фильтрация данных по статусу "EXECUTED"
    data = filter_data(data)
    print('Данные отфильтрованы')
    time.sleep(2)

    # Сортировка транзакций по времени выполнения от большей к меньшей
    data = sort_data(data)
    print('Данные отсортированы')
    time.sleep(2)
    # ФОрматирование даты в транзакции в вид ДД.ММ.ГГГГ
    data = data_format(data)
    print('Данные отфарматированы')
    time.sleep(2)
    # Вывод оследних 5 выполненных (EXECUTED) операций на экран.
    for transaction in data:
        print(transaction)
        time.sleep(1)


if __name__ == "__main__":
    main()
