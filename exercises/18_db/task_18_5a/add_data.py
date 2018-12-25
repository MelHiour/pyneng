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
from datetime import timedelta, datetime

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

def house_cleaning(db, how_old):
    result = []
    now = datetime.today().replace(microsecond=0)
    week_ago = now - timedelta(days = how_old)

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('select * from dhcp')
    result = cursor.fetchall()
    query = '''delete from dhcp where last_active = ?'''

    for row in result:
        if str(row[6]) < str(week_ago):
            print(row)
            cursor.execute(query, (row[6],))
            conn.commit()
            conn.close()
def dhcp_snoop_to_db(dhcp_list, db):
    print('Parsing output of dhcp snoop')
    host_parse = re.compile('(.+?)_')
    snoop_parse = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
 
    result = []
    now = str(datetime.datetime.today().replace(microsecond=0))

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
                    result_list.append(1)
                    result_list.append(now)
                    result.append(tuple(result_list))

    print('Establishing a DB connection')
    conn = sqlite3.connect(db)
    
    for row in result:
        try:
            with conn:
                print('Inserting :', row)
                query = '''insert into dhcp (mac, ip, vlan, interface, switch, active, last_active) values (?, ?, ?, ?, ?, ?, ?)'''
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
    
#dhcp_snoop_to_db(dhcp_snoop_files, db_filename)
#yaml_to_db('switches.yml', db_filename)
house_cleaning(db_filename, 7)
