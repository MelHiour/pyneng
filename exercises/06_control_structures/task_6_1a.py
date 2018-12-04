# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip_address = input('Please set the IP address: ')

address_correct = False

if len(ip_address.split('.')) == 4:
    for item in ip_address.split('.'):
        if item.isdigit() and int(item) in range(0,255):
            address_correct = True			
        else:
            address_correct = False
            break
else:
    address_correct = False

if not address_correct:
    print('Address NOK')

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

