'''
#=============================================================================
#     FileName: parseDNA.py 
#         Desc: One example 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 12/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-
import sys

def Acount(seq):
	return seq.upper().count('A')

def Tcount(seq):
	return seq.upper().count('T')

def Gcount(seq):
	return seq.upper().count('G')

def Ccount(seq):
	return seq.upper().count('C')

def GCcount(seq):
	return seq.upper().count('G') + seq.upper().count('C')

def GCcontent(seq):
	return 1.0 * GCcount(seq) / len(seq)

dna = raw_input("please input DNA sequence: ")

print Acount(dna)
print GCcount(dna)
print GCcontent(dna)
