# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

questions = {'access': 'Enter VLAN number: ', 'trunk': 'Enter allowed VLAN list: '}

# Input from user
int_type = input('Interface type: ')
int_number = input('Interface number: ')

vlans = input(questions[int_type])

# Set int_type equal to trunk_template or access_template via locals(). Basically, we use user prompt as part of varialbe name. Locals contains all definet variables.
int_type = locals()[int_type+'_template']

print('interface {}'.format(int_number))
print('\n'.join(int_type).format(vlans))


