'''
#=============================================================================
#     FileName: setup.py 
#         Desc: project of ex48 
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
	'description': "Ex48",
	'author': 'Honglong Wu',
	'url': 'https://github.com/Honglongwu/LPHW',
	'download_url': 'https://github.com/Honglongwu/LPHW',
	'author_email': 'wuhonglong@genomics.cn',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Ex48'],
	'scripts': [],
	'name': 'Ex48'
}

setup(**config)

