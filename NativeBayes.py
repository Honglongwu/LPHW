'''
#=============================================================================
#     FileName: NativeBayes.py 
#         Desc: This program was used to interpretation that theorem that how 
#		to calculate the probablity of p(A|B) when we know p(A), p(B),
#		and p(B|A). 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 22/04/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-
# Here is a running history for past week, for each day, it contains whether or not 
# the person ran, and whether or not they were tired

def NativeBayes(pa, pb, pba):
	'''
	this function was used to calculate the pba
	input: pa, pb, pba
	output: pab
	'''
	pab = pa * pba / pb
	return pab

def PA(RunRecord):
	'''
	calculate the tried ratio
	'''
	PA = 1.0 * len([d for d in RunRecord if d[1] == 'was tired']) / len(RunRecord)
	return PA

def PB(RunRecord):
	'''
	calcuate the run ratio
	'''
	PB = 1.0 * len([d for d in RunRecord if d[0] == 'ran']) / len(RunRecord)
	return PB

def PBA(RunRecord):
	'''
	calculate the ran ratio when he tired and ran
	'''
	PBA = 1.0 * len([d for d in RunRecord if d[0] == 'ran' and d[1] == 'was tired']) / len([d for d in RunRecord if d[1] == 'was tired'])
	return PBA

days = [["ran", "was tired"], ["ran", "was not tired"], ["didn't run", "was tired"], ["ran", "was tired"], ["didn't run", "was not tired"], ["ran", "was not tired"], ["ran", "was tired"]]

print "probability of being tired given that you ran:{0}".format(NativeBayes(PA(days), PB(days), PBA(days)))
