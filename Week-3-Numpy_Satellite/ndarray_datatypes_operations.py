# each ndarray has its own datatype (e.g. int, float etc.), and the 
# **datatypes matter** -> e.g. trying to assign a floating values to 
# an integer type element in an array will result in an error

import numpy as np

# .dtype method is used to get the datatype of an array
a1 = np.array([11, 12])
print(a1.dtype)

a2 = np.array([11.0, 12.0])
print(a2.dtype)

# you can also tell Python the datatype you want as below
a3 = np.array([11, 12], dtype=np.int64)
print(a3.dtype)

# as example this can be useful when you want to force floats into 
# integers (using floor function) as below
a4 = np.array([11.1, 12.7], dtype=np.int64)
print(a4.dtype,'\n')
print(a4)

# similarly we can force ints to be floats -> this is less problematic
# as we're not losing any information. may want to do this if you
# currently have integer data but expect them to change to floating
# data in the future
a5 = np.array([11, 21], dtype=np.float64)
print(a5.dtype,'\n')
print(a5)
print()

##############################################################

# below are examples of arithmetic operations on arrays. note that
# x is int, y is float. For most of our arithmetic operations,
# the result will be upcast to floating point, to avoid losing 
# precision.

# also note that arrays need the same dimensions for many of the below
# operations to work. (fine here as x, y dimenions = 2x2)

x = np.array([[111, 112], [121, 122]])
y = np.array([[211.1, 212.1], [221.1, 222.1]])

print(x)
print()
print(y)
print()

# add -> x00 is added with y00 to produce new x+y00 value etc. the
# results are floats to avoid losing precision
print(x + y)
print()
print(np.add(x, y))
print()

# subtract
print(x - y)
print()
print(np.subtract(x, y))
print()

# multiply
print(x * y)
print()
print(np.multiply(x, y))
print()

# divide
print(x / y)
print()
print(np.divide(x, y))
print()

# square root -> applies to all elements of the array
print(np.sqrt(x))
print()
print(np.sqrt(y))
print()

# exponent (e**x) -> applies to all elements of the array
print(np.exp(x))
print()
print(np.exp(y))