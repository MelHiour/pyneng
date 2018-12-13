# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''

from tabulate import tabulate
from task_12_2 import check_ip_availability

def ip_table(alive_ips, downs_ips):
    result = {'Reachable': alive_ips, "Unreachable:": down_ips}
    print(tabulate(result, headers = 'keys'))

alive_ips, down_ips = check_ip_availability('8.8.8.6-8')
ip_table(alive_ips, down_ips)
