# -*- coding: utf-8 -*-
'''
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к устройству, которому надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции, всегда будет передаваться только один из аргументов show, config, filename.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2
* filename - функция send_commands_from_file (ее надо написать по аналогии с предыдущими)

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и различных комбинация аргумента с командами:
    * списка команд commands
    * команды command
    * файла config.txt

'''

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]
command = 'sh ip int br'

import netmiko
import yaml
from pprint import pprint
from task_19_1 import send_show_command
from task_19_2 import send_config_command

def send_commands_from_file(device, script):
    result = {}
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            print('Connecting to {}'.format(device['ip']))
            ssh.enable()
            sent = ssh.send_config_from_file(script)
            result[device['ip']] = sent
        return result
    except netmiko.NetMikoAuthenticationException:
        return('Bad creds on {}'.format(device['ip']))
    except netmiko.NetMikoTimeoutException:
        return('Connection timeout to {}'.format(device['ip']))


def send_commands(device, show = False, filename = False, config = False):
    if show and not filename and not config:
        result = send_show_command(device, show)
        return result
    if config and not show and not filename:
        result = send_config_command(device, config)
        return result
    if filename and not show and not config:
        result = send_commands_from_file(device, filename)
        return result
    else:
        return('Band arguments assignment')

if __name__ == '__main__':
    with open('devices.yaml') as file:
        devices = yaml.load(file)
    for value in devices.values():
        for device in value:
            desired = send_commands(device, filename = 'config.txt')
            print(desired)


