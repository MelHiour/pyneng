# -*- coding: utf-8 -*-
'''
Задание 19.1b

Дополнить функцию send_show_command из задания 19.1a таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''
# -*- coding: utf-8 -*-
'''
Задание 19.1a

Переделать функцию send_show_command из задания 19.1 таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''
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

import netmiko 
import yaml
from pprint import pprint

with open('devices.yaml') as file:
    devices = yaml.load(file)

def send_show_command(device, command):
    result = {}
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            print('Connecting to {}'.format(device['ip']))
            print('\tPrompt is {}'.format(ssh.find_prompt()))
            if ssh.check_config_mode():
                print('\nIn config mode')
            else:
                print('Doing enable')
                ssh.enable()
                print('\tPrompt is {}'.format(ssh.find_prompt()))
            sent = ssh.send_command(command)
        result[device['ip']] = sent
        return result
    except netmiko.NetMikoAuthenticationException:
        return('Bad creds on {}'.format(device['ip']))
    except netmiko.NetMikoTimeoutException:
        return('Connection timeout to {}'.format(device['ip']))
if __name__ == '__main__':
    for value in devices.values():
        for device in value:
            result = send_show_command(device, command)
            print(result)
