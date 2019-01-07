# -*- coding: utf-8 -*-
'''
Задание 19.4a

Дополнить функцию send_commands_to_devices таким образом, чтобы перед подключением к устройствам по SSH,
выполнялась проверка доступности устройства pingом (можно вызвать команду ping в ОС).

> Как выполнять команды ОС, описано в разделе [subprocess](../../book/12_useful_modules/subprocess.md). Там же есть пример функции с отправкой ping.

Если устройство доступно, можно выполнять подключение.
Если не доступно, вывести сообщение о том, что устройство с определенным IP-адресом недоступно
и не выполнять подключение к этому устройству.

Для удобства можно сделать отдельную функцию для проверки доступности
и затем использовать ее в функции send_commands_to_devices.

'''

import netmiko
import yaml
import subprocess
from getpass import getpass
from pprint import pprint
from task_19_3 import send_commands

def send_commands_to_device(device_list, show = False, filename = False, config = False):
    reply = subprocess.run(['ping', '-c', '3', '-n', device_list['ip']], stdout = subprocess.DEVNULL)
    if reply.returncode == 0:
        username = input('Username:')
        password = getpass('Password:')
        secret = getpass('Enable secret:')
        device_list['username'] = username
        device_list['password'] = password
        device_list['secret'] = secret
        result = send_commands(device_list, show = show, filename = filename, config = config)
        return result
    else:
        return('The IP:{} id dead...'.format(device_list['ip']))

if __name__ == '__main__':
    command = 'sh ip int br'
    with open('devices2.yaml') as file:
        devices = yaml.load(file)
    for value in devices.values():
        for device in value:
            desired = send_commands_to_device(device, show = command)
            print(desired)
