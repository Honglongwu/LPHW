'''
#=============================================================================
#     FileName: PhoneSearch.py 
#         Desc: Dict
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 04/04/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

people = {'Alice':{'phone': '2341','addr': 'Foo drive 23'}, 'Beth':{'phone':'9102','addr':'Bar street 42'}, 'Cecil':{'phone':'3158','addr':'Benz avenue 90'}}

labels = {'phone': 'phone number', 'addr': 'address'}

name = raw_input('Name: ')

request = raw_input('Phone number(p) or address(a)?')

if request == 'p':
	key = 'phone'
if request == 'a':
	key = 'addr'

if name in people:
	print "%s's %s is %s" % (name, labels[key], people[name][key])
