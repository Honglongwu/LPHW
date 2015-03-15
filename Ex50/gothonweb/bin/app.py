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

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

# absolute path not the relative path
render = web.template.render('/Users/user/bin/GitHub/LPHW/Ex50/gothonweb/templates/')

class Index(object):
	def GET(self):
		form = web.input(name = "Nobody")
		greeting = "Hello, %s" % form.name
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()

