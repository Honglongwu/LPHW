'''
#=============================================================================
#     FileName: ex15.py 
#         Desc: file modules 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 05/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

from sys import argv
script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
