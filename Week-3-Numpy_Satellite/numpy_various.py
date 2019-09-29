import numpy as np

# arrays can be saved to disk as either binary or text format, and then
# subsequently loaded from disk

# as binary:
x = np.array([22.24, 24.24])
np.save('an_array', x)
print(np.load('an_array.npy'))

# as text:
np.savetxt('array.txt', X=x, delimiter=',')
# !cat array.txt 	# enter in console to view file contents ->	
print(np.loadtxt('array.txt', delimiter=','))

#######################################################

# below demonstrates Dot Product on Matrices and Inner Product on
# Vectors

# determine the dot product of two matrices (look up video.. unsure
# what a dot product is)
x2d = np.array([[2, 1], [1, 1]])
y2d = np.array([[5, 2], [3, 2]])
print(x2d.dot(y2d))
print('\n',np.dot(x2d,y2d))

# determine the inner product of two vectors
a1d = np.array([9 , 9 ])
b1d = np.array([10, 10])
print(a1d.dot(b1d))
print('\n',np.dot(a1d, b1d))

# dot produce on an array and vector
print(x2d.dot(a1d))
print('\n',np.dot(x2d,a1d))

#######################################################

# below demonstrates summing elements in an array
a1 = np.array([[11, 12], [21, 22]])

print(np.sum(a1))		# add all members
print(np.sum(a1, axis=0))	# columwise sum
print(np.sum(a1, axis=1))	# rowwise sum

#######################################################

# below demonstrates ***Element-wise functions***

x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)

# returns elementwise max between 2 arrays
print(np.maximum(x, y))

# below reshapes a 1x20 vector to become a 4x5 matrix
a1 = np.arange(20)
print(a1)
print(a1.reshape(4, 5))

# .transpose demonstrated below
a1 = np.array([[11, 12], [21, 22]])
print(a1.T)

# below demonstrates indexing using the .where method -> when true
# return x, flase return y
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([11, 22, 33, 44, 55])
filter = np.array([True, False, True, False, True])
out = np.where(filter, x1, y1)
print(out)

# further .where method below, returning new elements specified
# rather than existing elements in the matrixes
mat = np.random.rand(5,5)
out = np.where(mat >0.5, 1000, -1)
print(out)

# "any" or "all" conditionals demonstrated below
abools = np.array([True, False, True, True, False])
print(abools.any())
print(abools.all())

# below demonstrates Random Number Generation
y = np.random.normal(size = (1,5))[0] # not sure what index [0] does
print(y)
z = np.random.randint(low=2,high=50,size=4)
print(z)
print(np.random.permutation(z)) #returns a new ordering of z elements
print(np.random.uniform(size=4)) # returns a uniform distribution
print(np.random.normal(size=4)) # returns a normal distribution

# below demonstrates Merging Data Sets
k = np.random.randint(low=2,high=50,size=(2,2))
m = np.random.randint(low=2,high=50,size=(2,2))
print(k)
print(m)
# stacks matrices vertically
print(np.vstack((k, m)))
# stacks matrices horizontally)
print(np.hstack((k, m)))
# stacks verticaly using .concatenate method
print(np.concatenate([k, m], axis = 0))
# stacks horizontally using .concatenate method
print(np.concatenate([k, m.T], axis = 1))