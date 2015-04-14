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

# part 5: How to create plots(Histogram, scatter, boxplot)
Data visulization always helps us to understand the data easily. Python has library like matplotlib and seaborn to create multiple graphs effectively. Let us look at some of visulization to understand below behavior of variable:
1. the distribution of age 
2. relation between age and sales
3. if sales are normally distribution or not
	#### Histogram
	import matplotlib.pyplot as plt
	import pandas as pd
	df = pd.read_excel("E:/First.xlsx","Sheet1")
	
	# Plots in matplotlib reside within a figure object, use plt.figure to create new figure
	fig = plt.figure()

	# Create one or more subplots using add_subplot, because you can not create blank figure
	ax = fig.add_subplot(1,1,1)
	
	# variable
	ax.hist(df['Age'],bins=5)
	
	# Labels and Title
	plt.title('Age distribution')
	plt.xlabel('Age')
	plt.ylabel('#Employee')
	plt.show()
	
	#### Scatter
	fig = plt.figure()
	ax.scatter(df['Age'], df['Sales'])
	
	# labels and titles
	plt.title('Sales and Age distribution')
	plt.xlabel('Age')
	plt.ylabel('Sales')
	plt.show()
	
	#### boxplot
	import seaborn as sns
	
	sns.boxplot(df['Age'])
	sns.despine()
	
# part 6: How to generate frequency tables with pandas
Frequency Tables can be used to understand the distribution of a categorical variable or n categorical variables using frequency tables
	import pandas as pd
	df = pd.read_excel("E:/First.xlsx","Sheet1")
	print df
	
	test = df.groupby(['Gender','BMI'])
	test.size()

# part 7: How to do sample data set in python
To select sample of a data set, we will use library numpy and random. Sampling of dataset always helps to understand data quickly, let us say, from EMP table, I want to select random sample of 5 employee.
	import numpy as np
	import pandas as pd
	from random import sample
	
	# create random index
	rindex = np.array(sample(xrange(len(df)),5))
	
	# get 5 random rows from df
	dfr = df.ix[rindex]
	print dfr
	
# part 8: How to remove duplicate values of variable
often, we encounter duplicate observations. To tackle this in python, we can use dataframe.drop_duplicates()
	rem_dup = df.drop_duplicates(['Gender', 'BMI'])
	print rem_dup




# part 9: How to group variables in python to calculate count, average, sum
To understand the count, average and sum of variable, I would suggest you to use dataframe.describe() with groupby().
	test = df.groupby(['Gender'])
	test.describe()

# part 10: How to recognize and treat missing values and outliers
To identify missing values, we can use dataframe.isnull()
	df.isnull()
	
	# Example to impute missing values in Age by the mean
	import numpy as np
	meanAge = np.mean(df.Age)
	df.Age = df.Age.fillna(meanAge)
	
# part 11: How to join/merge data sets
Joining/merging is one of the common operation required to integrate datasets from different sources. They can be handled effectively in pandas using merge
df_new = pd.merge(df1, df2, how = 'inner', left_index = True, right_index = True)

# Another Manual
Here are some features of the library
1. A fast and efficient DataFrame object for data manipulation with integrated indexing
2. Tools for reading and writing data between in-memory data structures and different formats: csv, txt, excel, SQL database and HDF5
3. Flexible reshaping and pivoting of datasets
4. Intelligent label-based slicing, fancy indexing, and subsetting of large data sets
5. Columns can be inserted and deleted from data structures for size mutability
6. Time series-functionality: date range generation and frequency conversion
7. Aggregating or transforming data with a powerful group by engine allowing split-apply-combine operations on data sets

firstly, we should import the standard pandas libraries
	import pandas as pd
next we can read the data from csv file using read_csv function in pandas, and to view the summary head function will be useful
	insurance_rates = pd.read_csv("US_Homeinsurance_Rates.csv", delimiter = ",")
	insurance_rates.head()
syntax of sort:
	DataFrame.sort(columns=None, axis = 0, ascending = True, inplace = False, kind = 'quicksort', na_position = 'last')
	result.describe()
	result.mean()
	result.median()
we can easily add new columns to data frame. just say DataFrame['column_name'] = Value
	result['Percentage Change'] = (result['2013'] - result['2003']) * 100 / result['2003']

# pivot table
import pandas as pd
import numpy as np

df = pd.read_csv()
df['status'] = df['status'].astype("category")	
df['status'].cat.set_categories(['won','pending','present'], inplace = True)

pd.pivot_table(df, index = 'Name')
pd.pivot_table(df, index = ['Name', 'Rep', 'Manager'])
pd.pivot_table(df, index = ['Manager', 'Rep'], values = ['Prices'], aggfunc = [np.sum, len])
pd.pivot_table(df, index = ['Manager', 'Rep'], values = ['Prices'], columns = ['product'],aggfunc = [np.sum, len], fill_value = 0, margins = True)

table.query('Manager == ["Debra"]')

# 14 Best Python Pandas Features
Pandas is the most widely used tools for data munging. it contains high-level data structures and manipulation tools designed to make data analysis fast and easy.

# Loading the data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

olive_oil = pd.read_csv("file.csv")
olive_oil.head()

# Rename Function
olive_oil.rename(columns = {olive_oil.columns[0]:'area_Idili'}, inplace = True)
olive_oil.head()

# map
olive_oil.area_Idili = olive_oil.area_Idili.map(lambda x : x.split('.')[-1])

# apply and apply map
list_of_acids = ['','']
df = olive_oil[list_of_acids].apply(lambda x:x/100)

# shape and columns

