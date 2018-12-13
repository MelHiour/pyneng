# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess
from pprint import pprint
from tabulate import tabulate
from task_12_1 import check_ip_addresses

def check_ip_availability(ip_range):
    if '-' in ip_range:
       ip_range_dashed = ip_range.split('-')
       ip_main = '.'.join(ip_range_dashed[0].split('.')[0:3])
       if '.' in ip_range_dashed[1]:
           ip_start = ip_range_dashed[0].split('.')[-1]
           ip_stop = ip_range_dashed[1].split('.')[-1]

           list_of_ips = ['{}.{}'.format(ip_main, last_octet) for last_octet in range(int(ip_start), int(ip_stop)+1)]
       
       elif '.' not in ip_range_dashed[1]:
           ip_start = ip_range_dashed[0].split('.')[-1]
           ip_stop = ip_range_dashed[1]
           
           list_of_ips = ['{}.{}'.format(ip_main, last_octet) for last_octet in range(int(ip_start), int(ip_stop)+1)]
    
    else:
        list_of_ips = [ip_range]
    
    availability = check_ip_addresses(list_of_ips)
    return availability

if __name__ == '__main__':
    result = check_ip_availability('8.8.8.6-8')
    print(result)
