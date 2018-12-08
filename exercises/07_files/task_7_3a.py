# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('CAM_table.txt') as cam:
    result_lol = []
    for line in cam:
        if '.' in line:
            line_list = line.strip().split()
            line_list.remove('DYNAMIC')
            result_lol.append(line_list)
    result_lol.sort()
    for list in result_lol:
        print('   '.join(list))

