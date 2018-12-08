# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan = input('Enter VLAN ID: ')

with open('CAM_table.txt') as cam:
    file = cam.readlines()
    for line in file:
        if '.' in line:
            line_list = line.split()
            line_list.remove('DYNAMIC')
            if line_list[0] == vlan:
                print("   ".join(line_list))
