# nd arrays can be sliced similarly to lists and string

import numpy as np

# rank 2 array of shaoe (3, 4)
an_array = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
print(an_array)

# arguments for slicing is first all the rows you're after, and then 
# the columsn you're after. in below - is rows 0 and 1, and columns
# 1 and 2 (indexed by 0). After slicing, a_slice is part of an_array

# a slice has it's own indices once created - and these indices are
# different to the indices of an_array
a_slice = an_array[:2, 1:3]
print(a_slice)

# as both a_slice and an_array refer to the same underlying matrix
# in memory, when changes are made to elements in either of these 
# variables, the other variable will be effected - similar to how 
# when variables refering to the same list change when it is muted

# Remember, slices are just ferences to the same underlying data
print('Before:', an_array[0, 1])
a_slice[0 ,0] = 1000
print('After:', an_array[0, 1])

# to create a copy of an array assigned to a new variable, rather than 
# refering to the same underlying data, the slice can be fed in to 
# np.array

copyslice = np.array(an_array[:2, 1:3])
print(copyslice)

# thus when copyslice is changed, the underlying an_array remains 
# unaltered as copyslic is a copy - it is assigned to different
# underlying data
print('Before:', an_array[0, 1])
copyslice[0, 0] = 69
print('After:', an_array[0, 1])


##############################################################

an_array = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
print('\n',an_array)

# indexing with a single row returns a rank 1 array - it can be
# indexed with a single number
row_rank1 = an_array[1, :]
print('\n', row_rank1, row_rank1.shape)

# in contrast, when slicing, an array of the same rank as n_array
# will be generated (2d)
# note rank 2 arrays have double square brackets compared to 
# single square brackets for rank 1 arrays
row_rank2 = an_array[1:2, :]
print(row_rank2, row_rank2.shape)

# we can do the same for columns of an array:
col_rank1 = an_array[:, 1]
col_rank2 = an_array[:, 1:2]

print('\n',col_rank1, col_rank1.shape)
print('\n',col_rank2, col_rank2.shape)

##############################################################

# Array indexing for changing elements - sometimes its useful to 
# use an array of indexes to access or change elements

an_array = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33], 
					 [41, 42, 43]])

print('\nOriginal array:')
print(an_array)

col_indices = np.array([0, 1, 2, 0])
print('\nCol indices picked:', col_indices)

# .arrange method creates values up from 0 to the specified amount
row_indices = np.arange(4)
print('\nRow indices picked:', row_indices)

# similar to lists, zip can be used for iterating through multiple
# arrays at a time (in this case our index arrays)
for row, col in zip(row_indices, col_indices):
	print(row, ",", col)
	
# in below we are acessing elements in a matrix using arrays as
# indices
print('Values in the array at those indices:', 
	  an_array[row_indices, col_indices])

# we can also change elements of the matrix in the same way as below
# this will be useful in the course later on when we do data cleaning

an_array[row_indices, col_indices] += 100000
print('\nChanged array:')
print(an_array)

# Slice and Array Indexing is at the heart of NumPy