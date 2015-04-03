'''
#=============================================================================
#     FileName: Factorial.py 
#         Desc: iterate
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 04/04/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-
def factorial(n):
	if n == 1:
		return n
	else:
		return n * factorial(n - 1)

num = int(raw_input('which number do you want? '))
print factorial(num)
