'''
#=============================================================================
#     FileName: tests_sentence.py 
#         Desc: One example 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 14/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

from nose.tools import *
from Ex49 import lexicon
from Ex49 import sentence

def test_sentence_peek():
	setence.peek(lexicon.scan("north south east"))

def test_sentence_match():
	sentence.match(lexicon.scan("honglong go north south east"), 'verbs')

def test_sentence_skip():
	sentence.skip(lexicon.scan("honglong go north south east on the bear"), 'stops')

def test_sentence_parseverb():
	sentence.parse_verb(lexicon.scan("honglong go north south east on the bear"))

def test_sentence_parseobject():
	sentence.parse_object(lexicon.scan("honglong go north south east on the bear"))

def test_sentence_parsesubject():
	sentence.parse_subject(lexicon.scan("honglong go north south east on the bear"),'honglong')

def test_sentence():
	sentence.parse_sentence(lexicon.scan("honglong go north south east on the bear"))
