'''
#=============================================================================
#     FileName: ExtendNativeBayes.py 
#         Desc: This program was used to interpretation that theorem that how 
#		to calculate the probablity of p(y|x1,..., xn) when we know p(y), p(x1,...,xn),
#		and p(x1,...,xn|y). 
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

days = [["ran", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["ran", "was tired", "woke up early"]]

new_day = ["ran", "didn't wake up early"]

def calc_y_probability(y_label, days):
	return 1.0 * len([d for d in days if d[1] == y_label]) / len(days)

def calc_ran_probability_given_y(ran_label, y_label, days):
#	return 1.0 * len([d for d in days if d[0] == ran_label and d[1] == y_label]) / len([d for d in days if d[1] == y_label])
	return 1.0 * len([d for d in days if d[0] == ran_label and d[1] == y_label]) / len(days)

def calc_woke_probability_given_y(woke_label, y_label, days):
#	return 1.0 * len([d for d in days if d[2] == woke_label and d[1] == y_label]) / len([d for d in days if d[1] == y_label])
	return 1.0 * len([d for d in days if d[2] == woke_label and d[1] == y_label]) / len(days)

denominator  = 1.0 * len([d for d in days if d[0] == new_day[0] and d[2] == new_day[1]]) / len(days)

prob_tired = (calc_ran_probability_given_y(new_day[0], "was tired", days) * calc_woke_probability_given_y(new_day[1], "was tired", days) * calc_y_probability("was tired", days))/ denominator
prob_not_tired = (calc_ran_probability_given_y(new_day[0], "was not tired", days) * calc_woke_probability_given_y(new_day[1], "was not tired", days) * calc_y_probability("was not tired", days))/ denominator

classification = "was tired"
if prob_tired < prob_not_tired:
	classification = "was not tired"

print "Final classification for new day:{0}. Tired probability:{1}, Not tired probability:{2}".format(classification, prob_tired, prob_not_tired)
