'''
#=============================================================================
#     FileName: ex32.py 
#         Desc: List related operation
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 09/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# the first kind of for-loop goes through a list
for number in the_count:
	print "this is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that Lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Elements was: %d" % i

