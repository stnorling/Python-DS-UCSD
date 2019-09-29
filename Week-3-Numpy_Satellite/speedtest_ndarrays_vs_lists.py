from numpy import arange
from timeit import Timer

size = 1000000
timeits = 1000

# below creates an ndarray with values 0->size -1
nd_array = arange(size - 1)
print(type(nd_array))

# Timer expects the operation as a parameter
# here we pass nd_array.sum()
timer_numpy = Timer("nd_array.sum()", "from __main__ import nd_array")
print('Time taken by nump ndarray: %f seconds' %
	  (timer_numpy.timeit(timeits)/timeits))
  
# below we compare how long a list takes for the same computation
a_list = list(range(size))
print (type(a_list))

# here we pass sum(a_list) in to Timer
timer_list = Timer("sum(a_list)", "from __main__ import a_list")
print('Time taken by list: %f seconds' %
	  (timer_list.timeit(timeits)/timeits))