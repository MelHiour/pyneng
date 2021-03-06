# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip_address = input('IP Address: ')
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

# Join 1 (ones) to get the all ones in a subnet mask
mask_ones = ''.join(['1' for i in range(int(ip_address_splitted[1]))])
# Join 0 (zeroes) to get remaining zeroes in a subnet mask
mask_zeroes = ''.join(['0' for i in range (32-int(ip_address_splitted[1]))])
# Get a full binary mask like '11111111111111111111111100000000'
mask_bits=mask_ones+mask_zeroes

# Slice full bits in subnet mask by 8 and create a list. Convert binary to decimal integers.
mask_bits_list_int = [
int(mask_bits[0:8],2),
int(mask_bits[8:16],2),
int(mask_bits[16:24],2),
int(mask_bits[24:32],2)
]

# Split an IP address by period, create a list and convert every value in list to decimal integer.
ip_address_list = ip_address_splitted[0].split('.')
ip_address_list_int = [int(i) for i in ip_address_list]

# Form all necesary values for filling up the network template. Prefix and four octets of network address. It is created by binary (bitwise) AND operation. 10 AND 255 = 10, because 00001010 AND 11111111 = 00001010 
network_list_int = [
('/'+ip_address_splitted[1]),
mask_bits_list_int[0]&ip_address_list_int[0],
mask_bits_list_int[1]&ip_address_list_int[1],
mask_bits_list_int[2]&ip_address_list_int[2],
mask_bits_list_int[3]&ip_address_list_int[3]]

# Print the filled templates
print(template_net.format(ip_address_list_int))
print(template_mask.format(network_list_int))
