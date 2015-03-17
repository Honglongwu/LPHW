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


