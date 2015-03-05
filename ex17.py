'''
#=============================================================================
#     FileName: ex17.py 
#         Desc: file modules 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 06/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy file from %s to %s." % (from_file, to_file)

# we could do these two on one line, how?
#indata = open(from_file).read()
input = open(from_file, 'r')
indata = input.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit Return or CTRL-C to abort."

raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Aright, All done."

output.close()
input.close()

