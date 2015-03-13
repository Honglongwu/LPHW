'''
#=============================================================================
#     FileName: sentence.py 
#         Desc: One example 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 14/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

from Ex49 import lexicon

class ParserError(Exception):
	pass


class Sentence(object):
	
	def __init__(self, subject, verb, object):
	# remember we take ('noun', 'princess') tuples and convert them
	self.subject = subject[1]
	self.verb = verb[1]
	self.object = object[1]

def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
	
		if word[0]  == expecting:
			return word
		else:
			return None
	else:
		return None

def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)

def parse_verb(word_list):
	skip(word_list, 'stops')
	
	if peek(word_list) == 'verbs':
		return match(word_list, 'verbs')
	else:
		ParserError("Expected a verb next.")

def parse_object(word_list):
	skip(word_list, 'stops')
	next = peek(word_list)

	if next == 'nouns':
		return match(word_list, 'nouns')
	if next == 'directions':
		return match(word_list, 'directions')
	else:
		raise ParserError("Expected a noun  or directon next.")

def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj, verb, obj)

def parse_sentence(word_list):
	skip(word_list, 'stops')
	
	start = peek(word_list)
	
	if start == 'nouns':
		subj = match(word_list, 'nouns')
		return parse_subject(word_list, subj)
	elif start == 'verb':
		return parse_subject(word_list, ('nouns', 'player'))
	else:
		ParserError("Must start with subject, object, or verb not: %s" % start)

	
