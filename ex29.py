'''
#=============================================================================
#     FileName: ex29.py 
#         Desc: if condition excercise
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 08/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! the world is doomed!"
if people > cats:
	print "Not many cats! the world is saved!"
if people < dogs:
	print "the world is drooled on!"
if people > dogs:
	print "the world is dry!"

dogs += 5

if people >= dogs:
	print "people are greater than or equal to dogs."
if people <= dogs:
	print "people are less than or equal to dogs."

if people == dogs:
	print "people are dogs."
