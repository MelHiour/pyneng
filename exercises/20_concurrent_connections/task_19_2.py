# -*- coding: utf-8 -*-
'''
Задание 19.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет перечень команд в конфигурационном режиме на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

'''

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]

import netmiko 
import yaml
from pprint import pprint

def send_config_command(device, config_commands, verbose = True):
    result = {}
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            print('Connecting to {}'.format(device['ip']))
            ssh.enable()
            sent = ssh.send_config_set(config_commands)
            result[device['ip']] = sent
        if verbose:
            return result
    except netmiko.NetMikoAuthenticationException:
        return('Bad creds on {}'.format(device['ip']))

    except netmiko.NetMikoTimeoutException:
        return('Connection timeout to {}'.format(device['ip']))

if __name__ == '__main__':
    with open('devices.yaml') as file:
        devices = yaml.load(file)
    for value in devices.values():
        for device in value:
            result = send_config_command(device, commands)
            print(result)
