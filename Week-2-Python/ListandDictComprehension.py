# list comprehension

lst = [i**2 for i in range(1, 11)]
print(lst)

lst = [i for i in range(0,6)]
print(lst)

import random
lst = [random.randint(0, 5) for i in range(0, 10)]
print(lst)

# examples of dictionary comprehension

dict = {i: i**2 for i in range(1, 11)}
print(dict)

# example of dictionary comprehension to get letters A - Z and their corresponding ASCII values

dict = {chr(i) : i for i in range(65, 91)}
print(dict)
