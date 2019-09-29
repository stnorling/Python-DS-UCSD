# boolean indexing is used for conditional indexing of arrays

import numpy as np

an_array = np.array([[11, 12], [21, 22], [31, 32]])
print(an_array)

# below creates a boolean array which is boolean values based on the 
# condition of the numbers being > 15
filtarray = (an_array > 15)
print(filtarray)

# the created boolean array can now be used as indices to a larger
# array asking for values for which the filter is true -> effectively
# pulling out values that match a particular criteria
print(an_array[filtarray])

# this process can be done much simpler in one step as below. the
# conditional indices creates a boolean filter and then applies it
print(an_array[an_array > 15])

# the same can be done with more complex conditions. 
print(an_array[(an_array > 20) & (an_array < 30)])

# similarly even values could be obtained using modulo
print(an_array[(an_array % 2 == 0)])

# the elements can also be changed based on the conditon as below
# (only the elemenets that satisfy the condition change)
an_array[an_array % 2 == 0] +=100
print(an_array)