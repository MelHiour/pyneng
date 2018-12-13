# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(show_cdp):
    result = {}
    splitted_show = show_cdp.split('\n')
    for line in splitted_show:
        if line:
            local_device = line.split('>')[0]
            break
    
    for line in splitted_show[::-1]:
        if line:
            line_splitted = line.split()
            if line_splitted[0] != 'Device':
                if line_splitted[1][-1].isdigit():
                    remote_device, local_intf, *items, remote_intf = line_splitted
                    result[local_device, local_intf] = (remote_device, remote_intf)
                else:
                    remote_device, local_intf_pref, local_intf_num, *items, remote_intf_pref, remote_intf_num = line_splitted
                    result[local_device, local_intf_pref+local_intf_num] = (remote_device, remote_intf_pref+remote_intf_num)
            else:
                break
    return result

if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt') as file:
        oneline = file.read()

        result = parse_cdp_neighbors(oneline)
        print(result)
