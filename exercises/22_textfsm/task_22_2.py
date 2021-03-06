# -*- coding: utf-8 -*-
'''
Задание 22.2

В этом задании нужно использовать функцию parse_output из задания 22.1.
Она используется для того, чтобы получить структурированный вывод
в результате обработки вывода команды.

Полученный вывод нужно записать в CSV формате.

Для записи вывода в CSV, нужно создать функцию list_to_csv, которая ожидает как аргументы:
* список:
 * первый элемент - это список с названиями заголовков
 * остальные элементы это списки, в котором находятся результаты обработки вывода
* имя файла, в который нужно записать данные в CSV формате

Проверить работу функции на примере обработки
команды sh ip int br (шаблон и вывод есть в разделе).
'''
import csv
from task_22_1 import parse_output
from pprint import pprint

def list_to_csv(listed, csv_file):
    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(listed)

if __name__ == '__main__':
    file = open('output/sh_ip_int_br.txt').read()
    result = parse_output('templates/sh_ip_int_br.template', file)
    list_to_csv(result, '22_2.csv')
