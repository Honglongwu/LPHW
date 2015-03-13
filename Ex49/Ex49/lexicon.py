'''
#=============================================================================
#     FileName: lexicon.py 
#         Desc: One example 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 13/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

directions = {
	'north':'directions',
	'south':'directions',
	'east':'directions',
	'west':'directions',
	'down':'directions',
	'up':'directions',
	'left':'directions',
	'right':'directions',
	'back':'directions'
}

verbs = {
	'go': 'verbs',
	'stop': 'verbs',
	'kill': 'verbs',
	'eat': 'verbs'
}

stops = {
	'the':'stops',
	'in':'stops',
	'of':'stops',
	'from':'stops',
	'at':'stops',
	'it':'stops'
}

nouns = {
	'door': 'nouns',
	'bear': 'nouns',
	'princess': 'nouns',
	'cabinet': 'nouns'
}

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(sentence):
	words = sentence.split(' ')
	results = []
	for word in words:
		if convert_number(word):
			results.append(('numbers', convert_number(word)))
		elif nouns.get(word, 1) != 1:
			results.append((nouns.get(word), word))
		elif stops.get(word, 1) != 1:
			results.append((stops.get(word),word))	
		elif directions.get(word, 1) != 1:
			results.append((directions.get(word), word))
		elif verbs.get(word, 1) != 1:
			results.append((verbs.get(word), word))
		else:
			results.append(('error', word))
	return results

class

def main():
	sentences = raw_input("Please Input: ")
	print scan(sentences)

if __name__ == '__main__':
	main()	
