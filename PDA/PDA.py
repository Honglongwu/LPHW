'''
#=============================================================================
#     FileName: PDA.py
#         Desc: The basic pipeline of data analysis with python
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 18/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

# Import Data

import pandas as pd

data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
# df = pd.read_csv('d.csv') 
df = pd.read_csv(data_url)

# Data Transform
## 1. output the head and tail content
print df.head(n=2)
print df.tail(n=2)

## 2. output the names of columns and rows
print df.columns
print df.index

## 3. Trans the dataframe
print df.T

## 4. Reorder the data 
print df.sort(columns=["Apayao"])

## 5. Substract some columns of the data, you can use *ix* or *iloc*
print df.ix[:,0].head() # the first column (start with 0 not 1) and the fifth rows
print df.ix[10:20, 0:3] # or equal with df.ix[10:20, ['Abra', 'Apayao', 'Benguet']]

## 6. discard some rows or columns with *drop*
print df.drop(df.columns[[1, 2]], axis = 1).head() # axis = 0 stands for rows, axis = 1 stands for columns

# Summary information of Stat
## 1. Description
print df.describe()

## 2. Test, One perfect package of python that named as scipy contains more test functions, import stats module
from scipy import stats as ss
### Perform one sample t-test using 15000 as the true mean
print ss.ttest_1sample(a = df.ix[:,"Abra"], popmean = 15000) # output the t value and two-tailed p value

print ss.ttest_1sample(df, popmean = 15000) # apply this funtion to all columns

# Visulization, you can use matplotlib, seaborn or bokeh packages
import matplotlib.pyplot as plt
plt.show(df.plot(kind="box"))

import seaborn as sns
plt.show(sns.boxplot(df, width=0.5, color="paste1"))

plt.show(sns.violinplot(df, widths = 0.5, color = "pastel"))

plt.show(sns.distplot(df.ix[:,2], rug = True, bins = 15))

with sns.axes_style("white"):
    plt.show(sns.jointplot(df.ix[:,1], df.ix[:,2], kind = "kde"))

plt.show(sns.lmplot("Benguet", "Ifugao", df))

# Define Your Self-function
def add_2int(x, y):
	return x + y

print add_2int(2, 2)

def add_10(x):
	return x + 10

map(add_10, [1, 2, 3]) # or equal [add_10(i) for i in [1, 2, 3]]
filter(lambda x: x > 5, [3, 4, 5, 6, 7]) # or equal [x for x in [3, 4, 5, 6, 7] if x > 5]

# Create One Class
## create one sub-class that inherit from object class
class Human(object):
	### property that belongs this class
	species = "H. sapiens"
	
	### initial the class
	def __init__(self, name):
		### set value to the name
		self.name = name

	### example the class
	def say(self, msg):
		return "%s: %s" %(self.name, msg)

	### methods belong to all example
	@classmethod
	def get_species(cls):
		return cls.species

	### static methods don't need example
	@staticmethod
	def grunt():
		return "*grunt*"

i = Human(name="Ian")
print i.say("Hello")

j = Human("Jeol")
print j.say("hello")

#### use the class function
print i.get_species()

#### modify the property of class
Human.species = "H.neanderthalensis"
print i.get_species()
print j.get_species()

Human.grunt()

	
import numpy as np
#### create an array
np.array([1,2,3])
np.zeros(10)
np.ones(10)
np.eye((4,4))
b = np.arange(15)
b.shape
b.ndim
b.dtype

### Operations between arrays and scalars

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr * arr
arr - arr
arr + arr
arr ** 0.5
1 / arr


### Basic Indexing and Slicing
arr = np.array(10)
arr[5]
arr[5:8]
arr[5:8] = 12
arr[::2]
arr_slice = arr[5:8] # this not copy, just slicing a piece of data
arr_slice = 12 # that you will find arr[5:8] = 12
arr_slice = arr[5:8].copy()
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[0] # array([1,2,3]) row = axis 0; column = axis 1
arr2d[0][1] # 2
###
