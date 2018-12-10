# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif ' switchport mode access' in line:
                vlan = 1
                result_access[interface] = vlan
            elif line.startswith(' switchport access vlan '):
                vlan = line.split()[-1]
                result_access[interface] = vlan

    return result_trunk, result_access

result = get_int_vlan_map('config_sw2.txt')
print(result)

