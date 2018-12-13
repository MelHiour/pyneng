# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''


from draw_network_graph import draw_topology
from task_11_1 import parse_cdp_neighbors

topology_dict = {}

for file in ('sh_cdp_n_r1.txt',
            'sh_cdp_n_r2.txt',
            'sh_cdp_n_r3.txt',
            'sh_cdp_n_sw1.txt'):
    with open(file) as source:
        oneline = source.read()
        cdp_dict = parse_cdp_neighbors(oneline)
        for value in cdp_dict.values():
            if value in topology_dict.keys():
                pass
            else:
                topology_dict.update(cdp_dict)

print(topology_dict)

draw_topology(topology_dict)

