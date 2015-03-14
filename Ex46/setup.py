'''
#=============================================================================
#     FileName: setup.py 
#         Desc: project of ex46 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 12/03/2015
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
	'description': "Ex46",
	'author': 'Honglong Wu',
	'url': 'https://github.com/Honglongwu/LPHW',
	'download_url': 'https://github.com/Honglongwu/LPHW',
	'author_email': 'wuhonglong@genomics.cn',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Ex46'],
	'scripts': [],
	'name': 'Ex46'
}

setup(**config)

