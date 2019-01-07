# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_commands_threads, которая запускает функцию send_commands из задания 19.3 на разных устройствах в параллельных потоках.

Параметры функции send_commands_threads надо определить самостоятельно.
Должна быть возможность передавать параметры show, config, filename функции send_commands.

Функция send_commands_threads возвращает словарь с результатами выполнения команд на устройствах:

* ключ - IP устройства
* значение - вывод с выполнением команд

'''

import netmiko
import yaml
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from pprint import pprint

def send_show_command(device, command):
    result = {}
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        sent = ssh.send_command(command)
        result[device['ip']] = sent
    return result

def send_config_command(device, config_commands, verbose = True):
    result = {}
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            sent = ssh.send_config_set(config_commands)
            result[device['ip']] = sent
        if verbose:
            return result
    except netmiko.NetMikoAuthenticationException:
        return('Bad creds on {}'.format(device['ip']))

    except netmiko.NetMikoTimeoutException:
        return('Connection timeout to {}'.format(device['ip']))

def send_commands_from_file(device, script):
    result = {}
    try:
        with netmiko.ConnectHandler(**device) as ssh:
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

def send_commands_thread(devices, show = False, filename = False, config = False):
    result = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        multi = executor.map(send_commands, devices, repeat(show), repeat(filename), repeat(config))
    for item in multi:
        result.update(item)
    return result
        
if __name__ == '__main__':
    with open('devices.yaml') as file:
        devices = yaml.load(file)
    desired = send_commands_thread(devices['routers'], show = 'sh ip int br')
    pprint(desired)
