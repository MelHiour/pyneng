# -*- coding: utf-8 -*-
import sqlite3
from tabulate import tabulate
from sys import argv

db_filename = 'dhcp_snooping.db'

def get_full_dhcp():
    conn = sqlite3.connect(db_filename)
    result = []
    for row in conn.execute('select * from dhcp'):
        result.append(row)
    print(tabulate(result, tablefmt='fancy_grid'))
    conn.close()

def get_key_value(key, value):
    conn = sqlite3.connect(db_filename)
    conn.row_factory = sqlite3.Row

    query = 'select * from dhcp where {} = ?'.format(key)
    result = conn.execute(query, (value, ))
    for row in result:
        print('-' * 40)
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
    conn.close()

if len(argv) == 1:
    print('Return full talbe')
    get_full_dhcp()
elif len(argv) == 3:
    key, value = argv[1:]
    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    
    if key in keys:
        keys.remove(key)
        print('Return infor for {} {}'.format(key, value))
        get_key_value(key, value)
    else:
        print('Error. Supported key values are :', keys)
else:
    print('Error. Only two arguments are supported')







