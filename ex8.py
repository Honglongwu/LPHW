'''
#=============================================================================
#     FileName: ex8.py 
#         Desc: more excercises of print
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 04/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.",
		"That you could type up right.",	
		"But it didn't sing.",
		"So I said goodnight."
	)

