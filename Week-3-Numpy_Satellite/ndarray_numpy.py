# ndarrays are n-dimensional arrays of the same data type which are
# fast and space efficient

import numpy as np

an_array = np.array([3, 33, 333])

print(type(an_array))

# above array is 1 dimension, as shown using the .shape method. 
# because# of this, only 1 index is needed to access each element
print(an_array.shape)

print(an_array[0], an_array[1], an_array[2])

an_array[0] = 888

print(an_array)

# rank 2 array means 2 dimensions - e.g. becomes a matrix instead
# of a vector
rank2array = np.array([[11, 12, 13], [21,22, 23]])
print(rank2array)
print('\nThe shape is 2 rows, 3 columnts:', rank2array.shape)

print('\nAccessing elements [0, 0], [0, 1], and [1, 0] of the ndarray:',
	  rank2array[0, 0], rank2array[0, 1], rank2array[1, 0], '\n')


##########################################################

import numpy as np

# we can create an mxn array of zeros using the .zeros method as below
ex1 = np.zeros((2, 2))
print(ex1)

# .full method creates an array filled with the specified value

ex2 = np.full((2, 2), 9.0)
print(ex2)

# identity matrix can be created using the .eye method

ex3 = np.eye(2, 2)
print(ex3)

# an array of ones can be created using the .ones method

ex4 = np.ones((1, 2))
print(ex4)

# despite the above array seeming to be 1 dimension, it is in fact a 2 
# dimension array - this is because in order  to index it, 2 values 
# are required (i.e. [0, 1]). we can check this using the .shape method

print(ex4.shape)
print(ex4[0, 1])

# .random method can be used to create a random array of numbers
# below creates an array of random floats between 0 and 1
ex5 = np.random.random((2, 2))
print(ex5)