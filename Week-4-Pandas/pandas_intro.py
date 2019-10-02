# intro to Series and Dataframe datatypes in Pandas


import pandas as pd

#################### Pandas Series ####################

# pandas Series is a one-dimensional labeled array.

# below creates a pandas Series
ser1 = pd.Series(data = [100, 200, 300, 400, 500],
				 index = ['bob', 'jack', 'sam', 'denise', 'jim'])

# print details the series contents along with datatype of the data
print(ser1)

# 'data' and 'index' don't need to be specified when creating a 
# pandas Series - can simply enter the data as below - result is the same
ser1 = pd.Series([100, 200, 300, 400, 500],
				 ['bob', 'jack', 'sam', 'denise', 'jim'])
print(ser1)

# Note: - unlikely Numpy arrays, pandas Series can contain data
# with different datatypes (heterogenous data) - demonstrated below
# notice how datatype changes from int to object
ser1 = pd.Series([100, 'food', 300, 'swag', 500],
				 ['bob', 'jack', 'sam', 'denise', 'jim'])
print(ser1)

# .index method gives a list of all the Series indices
print(ser1.index)

# similar to dictionaries, indexing via indices returns the value for
# that location in the Series
# alternatively the .loc method can be used instead which serves the same
# purpose
print(ser1['sam'])
print(ser1.loc['denise'])

# we can also index by multiple indices at a time (put in rank 2 array)
print(ser1[['sam', 'denise']])
print(ser1.loc[['sam', 'denise']])

# we can also access data using numeric indices, as below
# the .iloc method achieves the same result
print(ser1[[4, 3, 1]])
print(ser1.iloc[[4, 3, 1]])

# we can check if an index exists within a Series using 'in'
print('bob' in ser1)

# python operations can also be applied to the Series data
print(ser1 * 2)
print(ser1[['bob', 'jim']] ** 2)

#################### Pandas DataFrames ####################

# pandas DataFrame is a 2-dimensional labeled data structure.

# if creating from scratch, the process is to first create a dictionary
# with key as the DataFrame column headers, and values as pandas Series 
# (with data and indices)
d = {'one' : pd.Series([100, 200, 300],
                       ['apple', 'ball', 'clock']),
    'two': pd.Series([111., 222., 333., 4444.],
                     ['apple', 'ball', 'cerill', 'dorothy'])
    }
# the Series and the dictionary are merged in the DataFrame 
# index labels within the series are merged as well
df1 = pd.DataFrame(d)
# empty values (indices with no assigned data) will show as NaN (not
# a number) when displayed in the DataFrame to indicicate there is no
# value
print(df1)

# similar to Series, DataFrame has the .index method 
print(df1.index)

# DataFrames also have the .columns method which lists the column
# headers along with their datatype
print(df1.columns)

# we can also use indexing to create DataFrames that are a subset
# of the full data available
df = pd.DataFrame(d, index=['apple', 'cerill', 'dorothy'])
print(df)

# columns can also be specified when indexing DataFrames (including 
# new columns that don't exist yet) - non existant columns will show 
# with data as NaN
df = pd.DataFrame(d, index=['apple', 'cerill', 'dorothy'],
                  columns=['two', 'five'])
print(df)

# DataFrames can also be created directly from a list of dictionaries.
# in this case, the keys get entered as column headers, and the values
# as data. the rows are indexed numerically from 0, incrementing per
# item (dictionary) in the list
data = [{'alex' : 1, 'joe' : 2},
        {'emma' : 5, 'dora' : 10, 'alice': 20}
        ]
df = pd.DataFrame(data)
print(df)

# index labels can be provided in such a DataFrame when it's created:
df = pd.DataFrame(data, index=['pets', 'books'])
print(df)

# as before, we can index this data by column header as well
df = pd.DataFrame(data, index=['pets', 'books'],
                  columns=['alex', 'alice', 'dora']
                  )
print(df)


# Below are examples of **basic DataFrame operations** - e.g. getting
# data out of a DataFrame
print(df1,'\n')

# indexing by a single column header yields a series object in return
print(df1['one'])

# using these columns, we can create new columns, and add or insert 
# them in to the DataFrame, as below
df1['three'] = df1['one'] * df1['two']
print(df1)

# logical operations can also be performed on columns, with results
# inserted in to new columns
df1['flag'] = df1['one'] > 250
print(df1)

# .pop method is used to remove columns from a DataFrame - it returns
# a series object of the column removed (can assign this to a variable)
dfpop = df1.pop('three')
print(dfpop)
print(df1)

# del funtion can also be used to delete columns (returns nothing)
del df1['two']
print(df1)

# .insert method is used to insert columns in to a DataFrame at a 
# specified location. arguments are (loc, column, value)
df1.insert(2, 'copy_of_one', df1['one'])
print(df1)

# when copying new columns in a DataFrame, we can also specify how
# much data we want from the source copied by slicing the data using
# indexing. values not copied show as NaN
df1['one_first_two'] = df1['one'][:2]
print(df1)














