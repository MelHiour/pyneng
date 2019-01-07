# -*- coding: utf-8 -*-
'''
Задание 20.1a

Переделать функцию из задания 20.1 таким образом,
чтобы она позволяла контролировать количество параллельных проверок IP.

Для этого, необходимо добавить новый параметр limit,
со значением по умолчанию - 2.

Функция должна проверять адреса из списка
таким образом, чтобы в любой момент времени максимальное количество
параллельных проверок было равным limit.

'''
# -*- coding: utf-8 -*-
'''
Задание 20.1

Переделать задание 19.4a таким образом, чтобы проверка доступности устройств
выполнялась не последовательно, а параллельно.

Для этого, можно взять за основу функцию check_ip_addresses из задания 12.1.
Функцию надо переделать таким образом, чтобы проверка IP-адресов выполнялась
параллельно в разных потоках.

'''

import netmiko
import yaml
import subprocess
from concurrent.futures import ThreadPoolExecutor
from getpass import getpass
from pprint import pprint
from task_19_3 import send_commands
from itertools import repeat


def check_ip_address(ip): # Argument is not iterable
    result = subprocess.run('ping -c 3 -n {}'.format(ip), shell=True, stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        return ip

def check_ip_threads(function, ips, limit=2):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(function, ips) # Map iterable entity with function
    return result

# Kind of a really bad code is started here...
def send_commands_to_device(devices, limit = 2, show = False, filename = False, config = False):
    username = input('Username:')
    password = getpass('Password:')
    secret = getpass('Enable secret:')
    
    ips = [device['ip'] for device in devices['routers']]
    pinger = list(check_ip_threads(check_ip_address, ips, limit))
    
    result_list = []
    for device in devices['routers']:
        if device['ip'] in pinger:
            device['username'] = username
            device['password'] = password
            device['secret'] = secret
            result = send_commands(device, show = show, filename = filename, config = config)
            result_list.append(result)
        else:
            print('{} is DOWN'.format(device['ip']))
    return result_list

if __name__ == '__main__':
    command = 'sh ip int br'
    with open('devices2.yaml') as file:
        devices = yaml.load(file)
    result = send_commands_to_device(devices, limit = 3, show = command)
    print(result)
