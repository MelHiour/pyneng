# -*- coding: utf-8 -*-
'''
Задание 22.4a

Переделать функцию из задания 22.4:
* добавить аргумент show_output, который контролирует будет ли выводится результат обработки команды на стандартный поток вывода
 * по умолчанию False, что значит результат не будет выводиться
* результат должен отображаться с помощью FormattedTable (пример есть в разделе)

'''
# -*- coding: utf-8 -*-
'''
Задание 22.4

На основе примера textfsm_clitable.py из раздела TextFSM
сделать функцию parse_command_dynamic.

Параметры функции:
* словарь атрибутов, в котором находятся такие пары ключ: значение:
 * 'Command': команда
 * 'Vendor': вендор (обратите внимание, что файл index отличается от примера, который использовался в разделе, поэтому вам нужно подставить тут правильное значение)
* имя файла, где хранится соответствие между командами и шаблонами (строка)
 * значение по умолчанию аргумента - index
* каталог, где хранятся шаблоны и файл с соответствиями (строка)
 * значение по умолчанию аргумента - templates
* вывод команды (строка)

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - названия столбцов
* значения - соответствующие значения в столбцах

Проверить работу функции на примере вывода команды sh ip int br.

Пример из раздела:
'''
from pprint import pprint
import clitable

def parse_command_dynamic(attributes, output, index = 'index', index_dir = 'templates', show_output = False):
    result = []
    cli_table = clitable.CliTable(index, index_dir)
    cli_table.ParseCmd(output, attributes)
    header = list(cli_table.header)
    data_rows = [list(row) for row in cli_table]
    for item in data_rows:
        zipped_dict = dict(zip(header, item))
        result.append(zipped_dict)
    if show_output:
        print(cli_table.FormattedTable())
    return result

if __name__ == '__main__':
    output = open('output/sh_ip_int_br.txt').read()
    attributes = {'Command': 'show ip interface brief', 'Vendor': 'cisco_ios'}
    result = parse_command_dynamic(attributes, output, show_output = True)
    pprint(result)
