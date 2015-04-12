# Ultimate Guide for Data exploration in python using Numpy, Matplotlib and Pandas

1. How to load data(files)
2. How to convert a variable to different data type
3. How to transpose a table
4. How to sort Data
5. How to create plots(Histogram, scatter, boxplot)
6. How to generate frequency tables
7. How to do sampling of Data set
8. How to remove duplicate values of a variable
9. How to group variables to calculate count, average, sum
10. How to recognize and treat missing values and outliers
11. How to merge/join data set effectively

# Part 1: How to load data(files)
Input data can be various format, such as txt, csv, xls, json. In python, it is easy to load data from any source, due to its simple syntax and availability of predefined libraries. Here, I will make use of pandas. it features a number of functions for reading tabular data as DataFrame object.
read_csv	read delimited data from a file. use comma as default delimiter
read_table	read delimited data from a file. use '\t' as default delimiter
read_excel	read data from excel
read_fwf	read data in fixed width column file
read_clipboard	read data from clipboard. useful for converting tables from web pages

loading data from csv file:
	import pandas as pd
	# Import pandas library
	df = pd.read_csv("E:/train.csv")
	# reading the dataset in a dataframe using pandas
	print df.head(3)

loading data from excel file:
	df = pd.read_excel("E:/EMP.xlsx","Data") # Data sheet of EMP file

loading data from txt file:
	df = pd.read_csv("E:/Text.txt", sep="\t")


