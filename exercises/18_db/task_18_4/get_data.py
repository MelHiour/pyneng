# -*- coding: utf-8 -*-
import sqlite3
from tabulate import tabulate
from sys import argv

db_filename = 'dhcp_snooping.db'

def get_full_dhcp():
    conn = sqlite3.connect(db_filename)
    result_active = []
    result_inactive = []
    for row in conn.execute('select * from dhcp where active = 1'):
        result_active.append(row)
    for row in conn.execute('select * from dhcp where active = 0'):
        result_inactive.append(row)
    print("Active")
    print(tabulate(result_active, tablefmt='simple'))
    print("Inactive")
    print(tabulate(result_inactive, tablefmt='simple'))
    
    conn.close()

def get_key_value(key, value):
    conn = sqlite3.connect(db_filename)
    conn.row_factory = sqlite3.Row

    query_active = 'select * from dhcp where {} = ? and active = 1'.format(key)
    result = conn.execute(query_active, (value, ))
    for row in result:
        print('-' * 40)
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))

    query_inactive = 'select * from dhcp where {} = ? and active = 0'.format(key)
    result = conn.execute(query_inactive, (value, ))
    for row in result:
        print('-' * 40)
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
    conn.close()

if len(argv) == 1:
    print('Return full table')
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







