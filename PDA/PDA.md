# Python For Data Analysis

## The Basic Pipeline of Data Anaylsis with Python
1. Import Data
   load the local Data or remote url file

2. Data transform
3. Summary information of Data, and display the description characteristic
4. Hypothesis test
	one simple t-test

5. Data Visulaization
	python package and R ggplot will give us more beatiful figure
6. Define self-function


## The Basic knowledge on Numpy
1. Basic info
   import numpy as np
   np.array([1, 2, 3])
   np.arange(10)
   np.empty()
   np.zeros()
   np.ones()
   np.empty()
   np.eye()

2. Operations
   arr = ([[1,2,3],[4,5,6]])
   1 / arr
   arr * arr
   arr - arr
   arr + arr
   arr ** 2
3. Boolean Indexing
   names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
   data = randn(7,4)
   data[names == 'Bob']
   data[names == 'Bob',:3]
   data[-(names == 'Bob')]
   // the python keywords and or do not work with boolean arrays

   // To set all the negative values in data to 0 we need only do:
   data[data < 0] = 0
   data[names != 'Joe'] == 7
4. Fancy Indexing
   arr = np.empty((8,4))
   arr[[4, 3, 0, 6]] 
   arr[[-3, -5, -7]]
   arr = np.arange(32).reshape((8, 4))
   arr[[1, 5, 7, 2], [0, 3, 1, 2]]
   arr[[1, 5, 7, 2], [:, 0, 3, 1, 2]] = arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]
5. Transposing Arrays and Swapping Axes
   arr = np.arange(15).reshape((3, 5))
   arr.T
   inner matrix product X^TX with np.dot
   arr = np.random.randn(6, 3)
   np.dot(arrT, arr)
6.Expressing Conditional Logic as Array Operations
   xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
   yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
   cond = np.array([True, False, True, True, False]) 
   result = [x if c else y for x, y, c in zip(xarr, yarr, cond)]
   result = np.where(cond, xarr, yarr)
   arr = randn(4, 4)
   np.where(arr > 0, 2, -2)
   np.where(arr > 0, 2, arr)
7. Methods for Boolean Arrays
   arr = randn(100)
   (arr > 0).sum # return the number of positive values
   bools = np.array([False, False, True, False])
   bools.any() # return True
   bools.all() # return False
8. Unique and Other Set Logic
   names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
   np.unique(names) # array(['Bob', 'Joe', 'Will'], dtype = '|S4')
   values = np.array([6, 0, 0, 3, 2, 5, 6])
   np.in1d(values, [2, 3, 6])
9. Linear Algebra
   x = np.array([[1,2,3],[4,5,6]])
   y = np.array([[6,23],[-1,7],[8,9]])
   x.dot(y) # np.dot(x,y)
   from numpy.linalg import inv, qr
   X = numpy.random.randn(5,5) 
   mat = X.T.dot(X)
   inv(mat)
   mat.dot(inv(mat))
10. Random Number Generation
   samples = np.random.normal(size=(4,4))
11. Reshaping Arrays
   arr = np.arange(8)
   arr.reshape((4,2))
   arr.reshape((4,2)).reshape((2,4))
   arr1 = np.array([[1,2,3],[4,5,6]])
   arr2 = np.array([[7,8,9],[10,11,12]])
   np.concatenate([arr1, arr2], axis=0) by rows
   np.concatenate([arr1, arr2], axis=0) by columns
   np.vstack((arr1, arr2))
   np.hstack((arr1, arr2))
12. Pandas Series
   import pandas as pd
   from pandas import Series, Dataframe
   obj = Series([4, 7, -5, 3])
   obj.values # array([4,7,-5,3])
   obj.index # Int64Index([0,1,2,3])
   obj2 = Series([4,7,-5,3], index=['d','b','a','c'])
   obj2['a'] # -5
   obj2['d'] = 6
   obj2[obj2 > 0]
   obj2 * 2
   np.exp(obj2)
13. Series as Dict
   'b' in obj2 # True
   'e' in obj2 # False
14. From Dict to Series
   sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon':16000, 'Utah': 5000}
   obj3 = Series(sdata)
   states = ['California', 'Ohio', 'Oregon', 'Texas']
   obj4 = Series(sdata, index=states)
   pd.isnull(obj4) or obj4.isnull()
   pd.notnull(obj4)
   obj3 + obj4 # automatically aligns differently-indexed data
   Both the series object itself and its index have a name attribute
15. Dataframe
   data = {'state':[],'year':, 'pop':[]}
   frame = dataframe(data)
   frame.year
   frame['state']
   # retrieve rows
   frame.ix['three']
   del frame['state']
   frame.values # will return the data contained in the dataframe
16. Index Objects
   index = obj.index
   index[1:]
17. reindex
   obj.reindex()
18. select row or column from dataframe
   obj[val] # select single column
   obj.ix[val] # select single row
   obj.ix[:, val] # select signle column of sunset of dataframe
   obj.ix[val1, val2] # select both row and column
19. arithmetic methods with fill values
   obj1 + obj2
   obj1.add(obj2, fill_value = 0)
   obj1.reindex(columns = df2.columns, fill_value = 0)
   frame.sub(series, axis=0) # 0 row-index 
20. Function application and mapping
   Numpy ufuncs work fine with pandas object
   frame = Dataframe()
   frame.abs()
   f = lambda x: x.max() - x.min()
   frame.apply(f, axis=0) # column
   frame.apply(f, axis=1) # rows
   def f(x):
	return Series([x.min(), x.max()], index=['min','max'])
   frame.apply(f)
   format = lambda x:'%.2f' % x
   frame.applymap(format)
   Series.map(format)
21. Sorting and Ranking
   frame.sort_index() # row index
   frame.sort_index(axis = 1) # column index
   frame.sort_index(axis = 1, ascending = False)
   obj = Series()
   obj.order() # any missing value are sorted to the end of the series object
   frame.sort_index(by='b')
   frame.sort_index(by=['b','a'])
   Series.rank(method="first")
   frame.rank(axis=1) # row
22. Summarizing and Computing Descriptive Statistics
   df.sum()
   df.sum(axis=1) 
   df.mean(axis = 1, skipna = False)
   df.idxmin() # return indirect statistics like the index value where the minimum or maximum values are attained
23. Data handle
   pd.read_csv
   pd.read_table
   data.to_csv 
24. Data Wrangling: clean, transform, merge, reshape
   pd.merge(df1, df2, on="key1", how="outer")
   pd.merge(left1, right1, left_on="key", right_index=True)
   pd.merge(left2, right2, how="outer", left_index=True, right_index=True)
   np.concatenate([arr, arr], axis=1) # column paste, as cbind() function of R
   pd.concat([s1,s2,s3]) # as rbind() function of R
   pd.concat([s1,s2,s3], axis=1) # dataframe
   df1.combine_first(df2)
25. Removing Duplicates
   data.duplicated()
   data.drop_duplicates()
   data.replace(target, value)
   pd.cut(list, bins)
   pd.value_count(pd.cut())
25. permutation and random sampling
   np.random.permutation()
   df.take()
    
