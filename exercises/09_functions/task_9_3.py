# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(config):
    
    result_trunk = {}
    result_access = {}
    
    with open(config) as file:
        for line in file:
            if line.startswith('interface '):
                interface = line.split()[-1]
            elif line.startswith(' switchport trunk allowed vlan'):
                vlans = line.split()[-1]
                result_trunk[interface] = [vlan for vlan in vlans.split('.')]
            elif line.startswith(' switchport access vlan '):
                vlan = line.split()[-1]
                result_access[interface] = vlan

    return result_trunk, result_access

result = get_int_vlan_map('config_sw1.txt')
print(result)                
