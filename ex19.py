'''
#=============================================================================
#     FileName: ex19.py 
#         Desc: def self-function 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 06/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheese!" % cheese_count
	print "you have %d boxes of crackers!" % boxes_of_crackers
	print "man, that's enough for a party."
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can do math inside too:"
cheese_and_crackers(10 + 20, 30 + 50)

print "we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


