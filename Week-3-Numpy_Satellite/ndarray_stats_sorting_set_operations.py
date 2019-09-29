# below covers more useful functions to be applied to matrices.
# covers common ndarray functions for doing data analysis, including 
# statistical, sorting, and set operations.

import numpy as np

# sets up random 2x5 matrix
a1 = 10 * np.random.randn(2, 5)
print(a1)

# below computes mean of all summed elements
print(a1.mean())

# below computes mean by row
print(a1.mean(axis = 1))

# and below computes mean by column
print(a1.mean(axis = 0))

# .sum method sums all of the elements in the matrix
print(a1.sum())

# below computes the medians. obtains per row as axis is set to 1
print(np.median(a1, axis = 1))

###############################################################

# set up unsorted array
a_unsorted = np.random.randn(10)
print(a_unsorted)

# some times we want to create a copy of an array and sort it
a_sorted = np.array(a_unsorted)
a_sorted.sort()

# we find that the copy is sorted, and the original is untouched
print(a_sorted)
print()
print(a_unsorted)
print()

# unique elelemts of an array an be pulled using the .unique method
a = np.array([1,2,1,4,2,1,4,2])
print(np.unique(a))
print()

################################################################

# below demonstrates set operations with np.array datatypes
s1 = np.array(['desk', 'chair', 'bulb'])
s2 = np.array(['lamp', 'bulb', 'chair'])
print(s1, s2)

# the .intersect1d method gives us elements that are common to both 
# arrays. it is 1d as intersect expects 1d arrays
print(np.intersect1d(s1, s2))

# the method .union yields all unique elements across both arrays
print(np.union1d(s1, s2))

# .different is used to yield elements in one set but not the other
# -> checks for x set elements not in y set
print(np.setdiff1d(s1, s2))

# similarly a set of booleans can be returned for whether each 
# element is in the x array is in the y array or not
print(np.in1d(s1, s2))