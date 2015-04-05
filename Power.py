'''
#=============================================================================
#     FileName: Power.py 
#         Desc: iterate
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 04/04/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-
def Power(x, n):
	if n == 0:
		return 1
	else:
		return x * Power(x, n - 1)
	
num = int(raw_input('which number do you want? '))
print Power(2, num)
print Power(3, num)

