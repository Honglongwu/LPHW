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
 

