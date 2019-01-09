# -*- coding: utf-8 -*-
'''
Задание 22.6

Это задание похоже на задание 22.5, но в этом задании подключения надо выполнять параллельно с помощью потоков.
Для параллельного подключения использовать модуль concurrent.futures.

В этом упражнении нужно создать функцию send_and_parse_command_parallel:
* она должна использовать внутри себя функцию send_and_parse_command
* какие аргументы должны быть у функции send_and_parse_command_parallel, нужно решить самостоятельно
* функция send_and_parse_command_parallel должна возвращать словарь, в котором:
 * ключ - IP устройства
 * значение - список словарей

Проверить работу функции send_and_parse_command_parallel на команде sh ip int br.

'''
from netmiko import ConnectHandler
import yaml
import clitable
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from pprint import pprint

def send_show_command(device, command):
    result = {}
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        sent = ssh.send_command(command)
    result[device['ip']] = sent
    return result

def parse_command_dynamic(attributes, output, index = 'index', index_dir = 'templates'):
    result = []
    cli_table = clitable.CliTable(index, index_dir)
    cli_table.ParseCmd(output, attributes)
    header = list(cli_table.header)
    data_rows = [list(row) for row in cli_table]
    for item in data_rows:
        zipped_dict = dict(zip(header, item))
        result.append(zipped_dict)
    return result

def send_and_parse_command(device, command, index = 'index', index_dir = 'templates'):
    attributes = {'Command': command, 'Vendor': 'cisco_ios'}
    result = {}
    show_sent = send_show_command(device, attributes['Command'])
    for ip, output in show_sent.items():
        parse_done = parse_command_dynamic(attributes, output)
        result[ip] = parse_done
    return result

def send_and_parse_command_parallel(devices, command, index = 'index', index_dir = 'templates', limit = 2):
    result = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        multi = executor.map(send_and_parse_command, devices, repeat(command))
    for item in multi:
        result.update(item)
    return result

test_command = "sh ip int br"
devices = yaml.load(open('devices.yaml'))
result = send_and_parse_command_parallel(devices['routers'], 'show ip interface brief')
pprint(result)
