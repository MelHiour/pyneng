# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
ip_address, mask = argv[1:]

template_net = '''
Network:
{0[0]:<8} {0[1]:<8} {0[2]:<8} {0[3]:<8}
{0[0]:08b} {0[1]:08b} {0[2]:08b} {0[3]:08b}
'''

template_mask = '''
Mask:
{0[0]}
{0[1]:<8} {0[2]:<8} {0[3]:<8} {0[4]:<8}
{0[1]:<08b} {0[2]:<08b} {0[3]:<08b} {0[4]:<08b}
'''

ones = ''.join(['1' for i in range(int(mask))])
zeroes = ''.join(['0' for i in range (32-int(mask))])
bits = ones+zeroes

bits_list = [
('/'+mask),
int(bits[0:8],2),
int(bits[8:16],2),
int(bits[16:24],2),
int(bits[24:32],2)]

ip_address_list = ip_address.split('.')
ip_address_list_int = [int(i) for i in ip_address_list]

print(template_net.format(ip_address_list_int))
print(template_mask.format(bits_list))
