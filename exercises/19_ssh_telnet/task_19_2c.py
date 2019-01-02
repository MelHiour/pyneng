# -*- coding: utf-8 -*-

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
                if 'Invalid input detected at' or 'Incomplete command' or 'Ambiguous command:' in sent:
                    err_mess = input('There is an error. Continue [y]/n:')
                    if err_mess == 'n':
                        return 'There is an error'
                        break
                    else:
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
            result = send_config_command(device, commands, verbose = True)
            pprint(result)
