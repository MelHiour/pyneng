# -*- coding: utf-8 -*-
'''
Задание 19.4

Создать функцию send_commands_to_devices (для подключения по SSH используется netmiko).

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В этой функции должен использоваться список словарей, в котором не указаны имя пользователя, пароль, и пароль на enable (файл devices2.yaml).

Функция должна запрашивать имя пользователя, пароль и пароль на enable при старте.
Пароль не должен отображаться при наборе.

Функция send_commands_to_devices должна использовать функцию send_commands из задания 19.3.

'''

import netmiko
import yaml
from getpass import getpass
from pprint import pprint
from task_19_3 import send_commands

def send_commands_to_device(device_list, show = False, filename = False, config = False):
    username = input('Username:')
    password = getpass('Password:')
    secret = getpass('Enable secret:')
    device_list['username'] = username
    device_list['password'] = password
    device_list['secret'] = secret
    result = send_commands(device_list, show = show, filename = filename, config = config)
    return result

if __name__ == '__main__':
    command = 'sh ip int br'
    with open('devices2.yaml') as file:
        devices = yaml.load(file)
    for value in devices.values():
        for device in value:
            desired = send_commands_to_device(device, show = command)
            print(desired)
