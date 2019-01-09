# -*- coding: utf-8 -*-
'''
Задание 22.1

Переделать пример, который использовался в разделе TextFSM, в функцию.

Функция должна называться parse_output. Параметры функции:
* template - шаблон TextFSM (это должно быть имя файла, в котором находится шаблон)
* output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов (в примере ниже, находится в переменной header)
* остальные элементы это списки, в котором находятся результаты обработки вывода (в примере ниже, находится в переменной result)

Проверить работу функции на каком-то из примеров раздела.

Пример из раздела:
'''

import sys
import textfsm
from tabulate import tabulate
from pprint import pprint

def parse_output(template, output):
    result = []
    with open(template) as file:
        fsm = textfsm.TextFSM(file)
    result.append(fsm.header)
    result.append(fsm.ParseText(output))
    return result

if __name__ == '__main__':
    file = open('output/sh_cdp_n_det.txt').read()
    result = parse_output('templates/sh_cdp_n_det.template',file)
    pprint(result)
'''
template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result, headers=header))
'''
