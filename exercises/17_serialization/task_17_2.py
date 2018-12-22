# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
from pprint import pprint

def parse_sh_cdp_neighbors(sh_cdp):
    '''Parsing of "show cdp neighbors" command'''
    result = {}
    # Regexp for             (R5)     (Fa0/1)   123    R S I      2820    (fa0/1)    
    int_parser = re.compile('(\w+) +([\w \/]+?) +\d+ [RTBSHIrP ]+ +\S+ +([\w \/]+)')
    # Regexp for SW1>
    host_parser = re.compile('(.+)>')
    local_hostname = host_parser.search(sh_cdp).group(1)
    # Result of findall is list of tuples three groups eash
    lists = int_parser.findall(sh_cdp)
    # Forming of complex dictionary 
    result[local_hostname] = {}
    for list in lists:
        result[local_hostname][list[1]]={list[0]:list[2]}
    return result

if __name__ == '__main__':
    # Just trying not to use "with" statement )
    file = open('sh_cdp_n_sw1.txt')
    sh_cdp = file.read()
    file.close()

    result = parse_sh_cdp_neighbors(sh_cdp)
    pprint(result)
