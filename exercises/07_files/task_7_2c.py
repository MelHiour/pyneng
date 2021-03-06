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

with open(argv[1]) as config, open(argv[2], 'w') as result:
    file = config.readlines()
    for line in file:
        for word in ignore:
            if word in line:
                break
            elif len(ignore)-1 == ignore.index(word):
                result.write(line)

