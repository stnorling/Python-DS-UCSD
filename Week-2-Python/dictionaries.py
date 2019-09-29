dict = {('Ghostbusters', 2016): 5.4, ('Ghostbusters', 1984): 7.8, ('Cars', 2006): 7.1}
print(dict)
# get method can be used to find values for items in a dictionary. Can be more useful than using
# dict[key] to retrieve an item using the key as an index, because if the key doesn't exist
# then an error will result. get retrieves None of the key doesn't exist
x = dict.get(('Cars', 2006))
print(x)
y = dict.get(('Toy Story', 1995))
print(y)

# in addition, 'in' can be used to check if a key is in a dictionary. returns True or False
print(('Toy Story', 1995) in dict)

# del and pop can be used to remove items from a dictionary using keys
print(dict.pop(('Ghostbusters', 2016)))
print(dict)

del dict[('Cars', 2006)]
print(dict)

dict = {('Ghostbusters', 2016): 5.4, ('Ghostbusters', 1984): 7.8, ('Cars', 2006): 7.1}

# to iterate through dictionary key value pairs, must use .items method
for k, v in dict.items():
    print(k, v)

# it is bad practice and not possible to iterate through data structures while they are
# being mutated. thus can be accomplished in 2 steps:
to_pop = []
# remember below is iterating through keys in the dictionary, and as the keys are tuples, i[1] refers
# to the second item in the tuple, e.g. the year of the movie
for i in dict:
    if i[1] < 2000:
        to_pop.append(i)

for i in to_pop:
    dict.pop(i)

print(dict)
