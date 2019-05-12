# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

with open(argv[1]) as config:
    file = config.read().split('\n')
    result_strings = (line for line in file if not any(word in line for word in ignore))
    for line in result_strings:
        if not line.startswith('!'):
            print(line)
