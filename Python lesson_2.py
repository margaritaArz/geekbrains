'''
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
 Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
'''

import csv
import re

def get_data():
    list_file = ['./resourses_csv/info_1.txt', './resourses_csv/info_2.txt', './resourses_csv/info_3.txt']
    list_data = [r'Изготовитель ОС:\s*([a-zA-Z]+)',
                 r'Название ОС:\s*([a-zA-Zа-яА-Я0-9 ]+)',
                 r'Код продукта:\s*([A-Z0-9\-]+)',
                 r'Тип системы:\s*([a-zA-Z-0-9\- ]+)']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for i in list_file:
        with open(i, encoding='cp1251') as f_n:
            f_n_reader = f_n.read()

            vendor = re.search(list_data[0], f_n_reader)
            if vendor:
                os_prod_list.append(vendor.group(1))
            else:
                os_prod_list.append('')

            name = re.search(list_data[1], f_n_reader)
            if name:
                os_name_list.append(name.group(1))
            else:
                os_name_list.append('')

            code = re.search(list_data[2], f_n_reader)
            if code:
                os_code_list.append(code.group(1))
            else:
                os_code_list.append('')

            type = re.search(list_data[3], f_n_reader)
            if type:
                os_type_list.append(type.group(1))
            else:
                os_type_list.append('')

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in range(0, len(os_type_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data

def write_to_csv(csv_file):
    main_data = get_data()
    if len(main_data) > 0:
        data_writer = csv.writer(csv_file)
        for row in main_data:
            data_writer.writerow(row)

with open('./result.csv', 'w') as file:
    write_to_csv(file)


'''
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в
файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''
import json


def write_order_to_json(item, quantity, price, buyer, date):
    order_dict = {
    'item': item,
    'quantity': quantity,
    'price': price,
    'buyer': buyer,
    'date': date
     }
    with open('orders.json', 'w') as info:
        json.dump(order_dict, info, indent=4)
    with open('orders.json') as info:
        print(info.read())


write_order_to_json(item='pen', quantity='1', price='1500', buyer='Mr.Ivanov', date='13.05.2019')


'''
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:

Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим
в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить
стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом:
allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
'''
import yaml

dict_yaml = {
    'key_1': [time, frame, advanced, new],
    'key_2': 2564,
    'key_3': {'price': '24$', 'money': '45§', 'porcent': '25%'}
}

with open('file.yaml', 'w', encoding='utf-16') as file_yaml:
    yaml.dump(dict_yaml, file_yaml, allow_unicode=True, default_flow_style=False)

with open('file.yaml','r', encoding='utf-16') as file_yaml:
    print(yaml.safe_load(file_yaml.read) == dict_yaml)
