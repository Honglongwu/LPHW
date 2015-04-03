'''
#=============================================================================
#     FileName: Fibs.py 
#         Desc: iterate
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 04/04/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-
def Fibs(num):
	result = [0, 1]
	for i in range(num-2):
		result.append(result[-2] + result[-1])
	return result

num = int(raw_input('how many numbers do you want? '))
print Fibs(num)
