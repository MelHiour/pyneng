# -*- coding: utf-8 -*-
'''
Задание 19.2b

В этом задании необходимо переделать функцию send_config_commands из задания 19.2a или 19.2 и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

При этом, параметр verbose также должен работать, но теперь он отвечает за вывод
только тех команд, которые выполнились корректно.

Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"

В файле задания заготовлены команды с ошибками и без:
'''

commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

import netmiko 
import yaml
from pprint import pprint

with open('devices.yaml') as file:
    devices = yaml.load(file)

def send_config_command(device, config_commands, verbose = True):
    result_correct = {}
    result_incorrect = {}
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            print('Connecting to {}'.format(device['ip']))
            ssh.enable()
            for command in config_commands:
                sent = ssh.send_config_set(command)
                if 'Invalid input detected at' in sent:
                    result_incorrect[command] = sent
                if 'Incomplete command' in sent:
                    result_incorrect[command] = sent
                if 'Ambiguous command:' in sent:
                    result_incorrect[command] = sent
                else:
                    result_correct[command] = sent
            if verbose:
                result = ((result_correct),(result_incorrect))
            else:
                result = ((result_incorrect))
            return result
    except netmiko.NetMikoAuthenticationException:
        return('Bad creds on {}'.format(device['ip']))

    except netmiko.NetMikoTimeoutException:
        return('Connection timeout to {}'.format(device['ip']))


if __name__ == '__main__':
    for value in devices.values():
        for device in value:
            result = send_config_command(device, commands, verbose = False)
            pprint(result)
