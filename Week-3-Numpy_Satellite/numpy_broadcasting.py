# broadcasting is used to perform operations on different sized
# ndarrays

# when operating on two arrays, numpy compares their shapes element-wise
# it starts with the trailing dimensions, and works its way forward.
# two dimensions are compatible when:
#	1. they are equal, or
#	2. one of them is 1 (scalar also applies as has 1 row, 1 column, 
#	   thus adding a scalar effectively uses broadcasing as well)

import numpy as np

a1 = np.zeros((4, 3))
print(a1)

add_rows = np.array([1, 0, 2])
print(add_rows)

# using broadcasting, each row of a1 is added to
y = a1 + add_rows
print(y)

add_cols = np.array([[0, 1, 2, 3]])
# .T method (transpose) is used to transpose the array from 1x4 to 4x1
add_cols = add_cols.T
print(add_cols)

# below each column, rather than row, is added to a1 using broadcasting
y = a1 + add_cols
print(y)

# adding a scalar (1x1) broadcasts in both direction
add_scalar = np.array([1])
print(a1 + add_scalar)