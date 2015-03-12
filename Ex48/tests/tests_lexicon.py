'''
#=============================================================================
#     FileName: tests_lexicon.py 
#         Desc: One example 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 13/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

from nose.tools import *
from Ex48 import lexicon

def test_directions():
	assert_equal(lexicon.scan("north"), [('directions', 'north')])
	results = lexicon.scan("north south east")
	assert_equal(results, [('directions', 'north'), ('directions', 'south'), ('directions', 'east')])

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verbs', 'go')])
	results = lexicon.scan("go kill eat")
	assert_equal(results, [('verbs', 'go'), ('verbs', 'kill'), ('verbs', 'eat')])

def test_stops():
	assert_equal(lexicon.scan("the"), [('stops', 'the')])
	results = lexicon.scan("the in of")
	assert_equal(results, [('stops', 'the'),('stops', 'in'), ('stops', 'of')])

def test_nouns():
	assert_equal(lexicon.scan("bear"), [('nouns', 'bear')])
	results = lexicon.scan("bear princess")
	assert_equal(results, [('nouns', 'bear'), ('nouns', 'princess')])

def test_numbers():
	assert_equal(lexicon.scan('1234'), [('numbers', 1234)])
	results = lexicon.scan("3 91234")
	assert_equal(results, [('numbers', 3), ('numbers', 91234)])

def test_errors():
	assert_equal(lexicon.scan("ADEG"), [('error', 'ADEG')])
	results = lexicon.scan("bear IAS princess")
	assert_equal(results, [('nouns', 'bear'), ('error', 'IAS'), ('nouns', 'princess')])
