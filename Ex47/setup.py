'''
#=============================================================================
#     FileName: setup.py 
#         Desc: project of ex47 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 13/03/2015
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
	'description': "Ex47",
	'author': 'Honglong Wu',
	'url': 'https://github.com/Honglongwu/LPHW',
	'download_url': 'https://github.com/Honglongwu/LPHW',
	'author_email': 'wuhonglong@genomics.cn',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Ex47'],
	'scripts': [],
	'name': 'Ex47'
}

setup(**config)

