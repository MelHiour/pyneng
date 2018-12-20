# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re

def parse_cfg(file):
   int_dict = {}
   regex = re.compile('interface (?P<intf>\S+)|ip address (?P<ipaddr>[\d.]+) (?P<mask>[\d.]+)')
   
   with open(file) as config:
       result = regex.finditer(config.read())
       for step in result:
           if step.lastgroup == 'intf':
                interface = step.group(step.lastgroup)
                int_dict[interface] = ()
           else:
                int_dict[interface] = (step.group('ipaddr'), step.group('mask'))
   return int_dict

if __name__ == '__main__':
    result = parse_cfg('config_r1.txt')
    print(result)
