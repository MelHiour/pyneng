# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Отправить команду command на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_show_command.

'''

command = 'sh ip int br'

from netmiko import ConnectHandler
import yaml
from pprint import pprint

def send_show_command(devices, command):
    result = {}
    for value in devices.values():
        for device in value:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                sent = ssh.send_command(command)
            result[device['ip']] = sent
    return result

if __name__ == '__main__':
    with open('devices.yaml') as file:
        devices = yaml.load(file)
    for value in devices.values():
        for device in value:
            result = send_show_command(device, command)
            print(result)
