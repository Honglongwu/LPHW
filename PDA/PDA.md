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
