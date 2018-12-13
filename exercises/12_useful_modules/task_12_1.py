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

def check_ip_addresses(ip_list):
    ip_alive = []
    ip_dead = []
    for ip in ip_list:
        result = subprocess.run('ping -c 3 -n {}'.format(ip), shell=True, stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            ip_alive.append(ip)
        else:
            ip_dead.append(ip)
    
    return ip_alive, ip_dead

if __name__ == '__main__':
    result = check_ip_addresses(['192.168.0.29','192.168.0.30', '8.8.8.8'])
    print(tabulate(result, headers = ['DEAD', 'ALIVE']))
