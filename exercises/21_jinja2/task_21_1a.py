# -*- coding: utf-8 -*-
'''
Задание 21.1a

Дополнить функцию generate_cfg_from_template из задания 21.1:

Функция generate_cfg_from_template должна принимать любые аргументы,
которые принимает класс Environment и просто передавать их ему.

То есть, надо добавить возможность контролировать аргументы trim_blocks, lstrip_blocks
и любые другие аргументы Environment через функцию generate_cfg_from_template.

Проверить функциональность на аргументах:
* trim_blocks
* lstrip_blocks

'''
# -*- coding: utf-8 -*-
'''
Задание 21.1

Переделать скрипт cfg_gen.py в функцию generate_cfg_from_template.

Функция ожидает два аргумента:
* путь к шаблону
* файл с переменными в формате YAML

Функция должна возвращать конфигурацию, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных data_files/for.yml.

'''

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os
from pprint import pprint

#$ python cfg_gen.py templates/for.txt data_files/for.yml
def generate_cfg_from_template(template_path, data_path, trim = True, lstrip = True):
    TEMPLATE_DIR, template_file = os.path.split(template_path)

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=trim, lstrip_blocks=lstrip)
    template = env.get_template(template_file)

    vars_dict = yaml.load(open(data_path))
    return(template.render(vars_dict))

if __name__ == '__main__':
    result = generate_cfg_from_template('templates/for.txt', 'data_files/for.yml', trim = False)
    print(result)
