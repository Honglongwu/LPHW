'''
#=============================================================================
#     FileName: ex33.py 
#         Desc: while loop 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 09/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
