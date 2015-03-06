#!/usr/bin/python
# - *- coding: utf-8 -*- 

def break_words(sentence):
	"""break the sentence"""
	return sentence.split(' ')

def count_words(sentence):
	"""count the words of one sentence."""
	return len(break_words(sentence))

sentence = "All good things coming together with bad news."

print break_words(sentence)
print count_words(sentence)
