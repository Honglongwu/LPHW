'''
#=============================================================================
#     FileName: ex31.py 
#         Desc: decision practice 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 08/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

print "You Enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a gaint bear here eating a cheese cake. what do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == 1:
		print "the bear eat your face off. Good job!"
	elif bear == 2:
		print "the bear eat your legs off. Good job!"
	else:
		print "Well, doing %s is probably better, Bears run away." % bear

elif door == "2":
	print "Your stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries"
	print "2. Yellow jecket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
	
else:
	print "You stumble around and fall on a knife and die, Good job!"
