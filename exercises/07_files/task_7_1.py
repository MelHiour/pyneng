# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
template = '''
Protocol:\t {0[0]}
Prefix:\t\t {0[1]}
AD/Metric:\t {0[2]}
Next-Hop:\t {0[4]}
Last update:\t {0[5]}
Interface:\t {0[6]}
'''
with open('ospf.txt') as file:
    ospf_txt =  file.readlines()
    for line in ospf_txt:
        line_splitted = line.rstrip().split()
        for item in line_splitted:
             if item == 'O':
                 line_splitted[line_splitted.index(item)] = 'OSPF'
             else:
                 line_splitted[line_splitted.index(item)] = line_splitted[line_splitted.index(item)].strip(',[]')

        print(line)
        print(template.format(line_splitted))


                 


