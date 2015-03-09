'''
#=============================================================================
#     FileName: ex41.py 
#         Desc: Dictionary 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 10/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-
from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
		"Nice job, You died ...jackass.",
		"Such a luser.",
		"I have a small puppy that's better at this."]
	print quips[randint(0, len(quips) - 1)]
	exit(1)

def central_corridor():
	print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
	print "Your entire crew. You are the last surviving member and your last"
	print "mission is to get the neutron destruct bomb from the Weapons Armory,"
	print "put it in the bridge, and blow the ship up after getting into an "
	print "escape pod."
	print "\n"
	print "You are running down the central corridor to the weapons armooy when"
	print "a gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
	print "flowing around his hate filled body. He's blocking the door to"
	print "Armory and about to pull a weapon to blast you."

	action = raw_input("> ")
	
	if action == "shoot!":
		print "Quick on the draw you yank out your blaster and fire it at the gothon."
		print "His clown costume is flowing and moving around his body, which throws"
		print "off your aim. Your laser hits his costume but misses him entirely. This"
		print "completely ruins his brand new costume his mother bought him, which"
		print "makes him fly into an insane rage and blast you repeatly in the face until"
		print "you are dead. Then he eats you."
		print 'death'

	elif action == "dodge!":
		print "Like a world class boxer you dodge, weave, slip and slide right"
		print "as the gothon's blaster cranks a laser past your head."
		print "In the middle of your artful dodge your foot slips and you"
		print "bang your head on the metal wall and pass out."
		print "You wake up shortly after only to die as the gothon stomps on"
		print "your head and eats you."
		print 'death'
	
	elif action == "tell a joke":
		print "Lucky for you they made learn gothon insults in the academy."
		print "You tell the one Gothon joke you know:"
		print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
		print "The gothon stops, tries not to laugh, then busts out laughing and can't move."
		print "While he's laughing you run up and shoot him square in the head"
		print "putting him down, then jump through the weapon armory door."
		print 'laser_weapon_armory'
	else:
		print "DOES NOT COMPUTE!"
		print 'central_corridor'

def laser_weapon_armory():
	print "you do a dive roll into the weapon armory, crouch and scan the room"
	print "for more gothons that might be hiding. It's dead quiet, too quiet."
	print "You stand up and run to the far side of the room and find the"
	print "neutron bomb in its container. There's a keypad lock on the box"
	print "and you need the code to get the bomb out. if you get the code"
	print "wrong 10 times then the clock closes forever and you can't"
	print "get the bomb. the code is 3 digits."
	
	code = "%d%d%d" %(randint(1, 9), randint(1, 9), randint(1, 9))
	guess = raw_input("[keypad]> ")
	guess = 0

	while guess != code and guess < 10:
		print "BZZZZEDD!"
		guesses += 1
		guess = raw_input("[keypad]> ")
	
	if guess == code:
		print "The container clicks open and the seal breaks, letting gas out"
		print "You grab the neutron bomb and run as fast as you can to the"
		print "bridge where you must place it in the right spot."
		return 'the_bridge'
	
	else:
		print "The lock buzzes one last time and then you hear a sickening"
		print "melting around as the mechanism is fused together."
		print "You decide to sit there, and finally the gothons blow up the"
		print "ship from their ship and you die."
		print 'death'

def the_bridge():
	print "You burst Onto the Bridge with neutron destruct bomb"
	print "under your arm and surprise 5 gothons who are trying to"
	print "take control of the ship. Each of them has an even uglier"
	print "clown costume than the last. They haven't pulled their"
	print "weapons out yet, as they see the active bomb under your"
	print "arm and don't want to set it off."
	
