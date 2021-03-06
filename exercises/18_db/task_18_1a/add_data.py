# -*- coding: utf-8 -*-
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import glob
import sqlite3
import re
import yaml
import os

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print(dhcp_snoop_files)

def dhcp_snoop_to_db(dhcp_list, db):
    print('Parsing output of dhcp snoop')
    host_parse = re.compile('(.+?)_')
    snoop_parse = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
 
    result = []
    db_exists = os.path.exists(db)
    
    if not db_exists:
        return print('DB is not exist')

    for file in dhcp_list:
        print('Parsing ', file)
        hostname = host_parse.search(file).group(1)
        with open(file) as shoop:
            for line in shoop:
                match = snoop_parse.search(line)
                if match:
                    result_list = []
                    result_list = list(match.groups())
                    result_list.append(hostname)
                    result.append(tuple(result_list))

    print('Establishing a DB connection')
    conn = sqlite3.connect(db)
    
    for row in result:
        try:
            with conn:
                print('Inserting :', row)
                query = '''insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('An error occured: ', e)
    conn.close()

def yaml_to_db(yaml_file, db):
    print('Parsing YAML file {}'.format(yaml_file))
    
    db_exists = os.path.exists(db_filename)
    if not db_exists:
        return print('DB is not exists')
        

    to_db = []
    
    with open(yaml_file) as file:
        result = yaml.load(file)
        for value in result.values():
            for key, value in value.items():
                to_db.append(tuple([key, value]))

    print('Establishing a DB connection')
    conn = sqlite3.connect(db)

    for row in to_db:
        try:
            with conn:
                print('Inserting :', row)
                query = '''insert into switches (hostname, location) values (?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('An error occured: ', e)
    conn.close()
   
dhcp_snoop_to_db(dhcp_snoop_files, db_filename)
yaml_to_db('switches.yml', db_filename)
