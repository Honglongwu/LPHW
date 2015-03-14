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
	assert_raises(sentence.ParserError, sentence.peek, lexicon.scan("north south east"))

def test_sentence_match():
	assert_raises(sentence.ParserError,sentence.match, lexicon.scan("go north south east"), 'verbs')

def test_sentence_skip():
	assert_raises(sentence.ParserError,sentence.skip, lexicon.scan("on bear"), 'stops')

def test_sentence_parseverb():
	assert_raises(sentence.ParserError,sentence.parse_verb, lexicon.scan("go north south east"))

def test_sentence_parseobject():
	assert_raises(sentence.ParserError,sentence.parse_object, lexicon.scan("go north south east"))

def test_sentence_parsesubject():
	assert_raises(sentence.ParserError, sentence.parse_subject, lexicon.scan("north south east on the bear"),'honglong')

def test_sentence():
	assert_raises(sentence.ParserError, sentence.parse_sentence, lexicon.scan("go north south east on the bear"))
