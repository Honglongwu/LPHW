'''
#=============================================================================
#     FileName: setup.py 
#         Desc: project of ex49 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 14/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = 
{
	'description': "Ex49",
	'author': 'Honglong Wu',
	'url': 'https://github.com/Honglongwu/LPHW',
	'download_url': 'https://github.com/Honglongwu/LPHW',
	'author_email': 'wuhonglong@genomics.cn',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Ex49'],
	'scripts': [],
	'name': 'Ex49'
}

setup(**config)

