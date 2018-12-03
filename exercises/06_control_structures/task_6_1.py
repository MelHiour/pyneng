# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_address = input('Please set the IP address: ')

class_a = (1, 127)
class_b = (128, 191)
class_c = (192, 223)
class_d = (224, 239)



if int(ip_address.split('.')[0]) in class_a \
or int(ip_address.split('.')[0]) in class_b \
or int(ip_address.split('.')[0]) in class_c:
    print('IP address {} belongs to Unicast'.format(ip_address))
elif int(ip_address.split('.')[0]) in class_d:
    print('IP address {} belongs to Multicast'.format(ip_address))
elif ip_address == '255.255.255.255':
    print('IP address {} is Local broadcast'.format(ip_address))
elif ip_address == '0.0.0.0':
    print('IP address {} is Local unassigned'.format(ip_address))
else:
    print('IP address {} is unused'.format(ip_address))

