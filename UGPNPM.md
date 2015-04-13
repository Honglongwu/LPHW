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

# Part 2: How to convert variables to different type
Converting a variable data type to other is import and common procedure we perform after loading data.

Convert numeric variables to string variables and vice versa 
	string_outcome = str(numeric_input) 
	integer_outcome = int(string_input)
	float_outcome = float(string_input)
the later operations are especially useful when you input value from user using raw_input(), by default, the values are read at string.

Convert character date to Date:
there are multiple ways to do this. the simplest would be to use datetime library and strptime function.
	from datetime import datetime
	char_date = 'Apr 1 2015 1:20 PM'
	date_obj = datetime.strptime(char_date, "%b %d %Y %I:%M%p")
	print date_obj
	
# part 3: How to transpose a Data set
	long to wide
	df = pd.read_excel("E:/transpose.xlsx", "Sheet1")
	print df
	result = df.pivot(index = "ID", columns = "Product", values = "Sales")
	print result

# part 4: How to sort DataFrame
Sorting of data can be done using dataframe.sort(). It can be based on multiple variables and ascending or descending both order.
	df = pd.read_excel("E:/transpose.xlsx","Sheet1")
	print df.sort(['Product', 'Sales'], ascending = [True, False])


