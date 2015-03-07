'''
#=============================================================================
#     FileName: ex30.py 
#         Desc: if/elif/else practice 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 08/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if buses < people:
	print "Aright, Let's just take the buses."
else:
	print "Fine, let's stay home then."
