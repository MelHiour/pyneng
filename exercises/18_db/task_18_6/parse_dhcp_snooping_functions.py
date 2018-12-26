import sqlite3
import os
import yaml
import re
from tabulate import tabulate

def create_db(db_name, db_schema):
    db_exists = os.path.exists(db_name)
    conn = sqlite3.connect(db_name)
    if not db_exists:
        print('///Creating schema...')
        with open(db_schema) as file:
            db_schema = file.read()
        conn.executescript(db_schema)
        print('\tDB has been created')
    else:
        print('\tDatabase exists')

def add_data_switches(db, yaml_file):
    print('///Parsing YAML file {}'.format(yaml_file))
    db_exists = os.path.exists(db)
    if not db_exists:
        return print('DB is not exists')
    to_db = []
    with open(yaml_file[0]) as file:
        result = yaml.load(file)
        for value in result.values():
            for key, value in value.items():
                to_db.append(tuple([key, value]))
    print('\tEstablishing a DB connection')
    conn = sqlite3.connect(db)
    for row in to_db:
        try:
            with conn:
                print('\tInserting :', row)
                query = '''insert into switches (hostname, location) values (?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('An error occured: ', e)
    conn.close()

def add_data(db, dhcp_list):
    print('\\\Parsing output of dhcp snoop')
    host_parse = re.compile('(.+?)_')
    snoop_parse = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result = []
    db_exists = os.path.exists(db)
    if not db_exists:
        return print('DB is not exist')
    for file in dhcp_list:
        print('\tParsing ', file)
        hostname = host_parse.search(file).group(1)
        with open(file) as shoop:
            for line in shoop:
                match = snoop_parse.search(line)
                if match:
                    result_list = []
                    result_list = list(match.groups())
                    result_list.append(hostname)
                    result.append(tuple(result_list))
    print('\tEstablishing a DB connection')
    conn = sqlite3.connect(db)
    for row in result:
        try:
            with conn:
                print('\tInserting :', row)
                query = '''insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('An error occured: ', e)
    conn.close()

def get_data(db_name, key, value):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    query = 'select * from dhcp where {} = ?'.format(key)
    result = conn.execute(query, (value, ))
    for row in result:
        print('-' * 40)
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
    conn.close()

def get_all_data(db_name):
    conn = sqlite3.connect(db_name)
    result = []
    for row in conn.execute('select * from dhcp'):
        result.append(row)
    print(tabulate(result, tablefmt='fancy_grid'))
    conn.close()


