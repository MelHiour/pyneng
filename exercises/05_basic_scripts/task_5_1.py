
# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_address = input('Specify the IP address with mask: ')
ip_address_splitted = ip_address.split('/')

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

ones = ''.join(['1' for i in range(int(ip_address_splitted[1]))])
zeroes = ''.join(['0' for i in range (32-int(ip_address_splitted[1]))])
bits = ones+zeroes

bits_list = [
('/'+ip_address_splitted[1]),
int(bits[0:8],2),
int(bits[8:16],2),
int(bits[16:24],2),
int(bits[24:32],2)]

ip_address_list = ip_address_splitted[0].split('.')
ip_address_list_int = [int(i) for i in ip_address_list]

print(template_net.format(ip_address_list_int))
print(template_mask.format(bits_list))
