'''
#=============================================================================
#     FileName: ex18.py 
#         Desc: def self-function 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 06/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print print_two("Zed", "Shaw")
print print_two_again("Zed", "Shaw")
print print_one("Honglong")
print print_none()

