# -*- coding: utf-8 -*-
'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
import yaml
from pprint import pprint
from draw_network_graph import draw_topology

with open('topology.yaml') as topo:
    from_yaml = yaml.load(topo)

'''
from_yaml looks like this:
    {'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}},

     'R2': {'Eth 0/0': {'SW1': 'Eth 0/2'},
            'Eth 0/1': {'R5': 'Eth 0/0'},
            'Eth 0/2': {'R6': 'Eth 0/1'}},
     ...
We need to convert it to smth like this:
    ('R1', 'Eth 0/0'):('SW1', 'Eth 0/1')
    ('R2', 'Eth 0/0'):('SW1', 'Eth 0/2')
    ('R2', 'Eth 0/1'):('R5', 'Eth 0/0')
    ...
'''
topology_dict = {}
for local_host, topo in from_yaml.items():
    for local_interface, remote in topo.items():
        for remote_host, remote_interface in remote.items():
            topology_dict[(local_host, local_interface)] = (remote_host, remote_interface)


'''
topology_dict has duplicates
{('R1', 'Eth 0/0'): ('SW1', 'Eth 0/1'),
...
('SW1', 'Eth 0/1'): ('R1', 'Eth 0/0'),

We need to clear them. 
Form a new dictionary, if key is not in values in new dict, add this key-value pair to new dict.
'''
topology_cleared = {}
for key, value in topology_dict.items():
    if key not in topology_cleared.values():
        topology_cleared[key] = value

draw_topology(topology_cleared)

