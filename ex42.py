'''
#=============================================================================
#     FileName: ex42.py 
#         Desc: class 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 11/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

class TheThing(object):
	
	def __init__(self):
		self.number = 0
	
	def some_function(self):
		print "I got called."

	def add_me_up(self, more):
		self.number += more
		return self.number

# two different thing
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print a.add_me_up(28)
print b.add_me_up(30)
print b.add_me_up(30)

print a.number
print b.number
