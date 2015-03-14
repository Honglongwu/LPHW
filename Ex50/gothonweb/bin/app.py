'''
#=============================================================================
#     FileName: app.py 
#         Desc: project of one game that run on the web page 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 15/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

import web

urls = ('/', 'index')

app = web.application(urls, globals())

class index:
	def GET(self):
		greeting = "hello world"
		return greeting

if __name__ == '__main__':
	app.run()
