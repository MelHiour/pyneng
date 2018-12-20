# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re
#from task_15_3a import parse_cfg

def parse_cfg(file):
    int_dict = {}
    regex = re.compile('interface (?P<intf>\S+)|ip address (?P<ipaddr>[\d.]+) (?P<mask>[\d.]+)')

    with open(file) as config:
        result = regex.finditer(config.read())
        for step in result:
            if step.lastgroup == 'intf':
                interface = step.group(step.lastgroup)
                int_dict[interface] = []
            else:
                int_dict[interface].append((step.group('ipaddr'), step.group('mask')))
    return int_dict

result = parse_cfg('config_r2.txt')
print(result)
