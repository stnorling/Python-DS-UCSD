# sets only allow unique elements (no duplicates)
# they are unordered like dictionaries, and as such run very quickly
# sets also support useful set operations, such as union and intersection

sams_colours = set(['green', 'brown', 'yellow'])
# due to the unordered nature of sets, the order of the printed set can be
# different to the order of the items above
print(sams_colours)
print(type(sams_colours))

sams_colours.add('blue')
print(sams_colours)

# trying to add an already existing value does nothing as the set cannot hold
# duplicate values
sams_colours.add('green')
print(sams_colours)

# .remove and .discard methods can be used to take away items from the set
# .remove can be seen as preferable, because if you try to remove an item
# that doesn't exist in the set - it will do nothing, whereas .discard will result
# in an error
sams_colours.discard('brown')

denises_colours = set(['brown', 'blue', 'green', 'red'])

# set method .union return items that exist in either of the sets - useful if you
# want to know all the unique items in two separate sets. duplicate values appear
# only once in the result
either = denises_colours.union(sams_colours)
print(either)

# to find unique items in common between 2 sets, the intersection method is used
both = denises_colours.intersection(sams_colours)
print(both)

# rather than use the union and intersection methods, the '|'' operator and '&' operator
# can be used instead. e.g. as below

all_colours = denises_colours | sams_colours
print(all_colours)

same_colours = denises_colours & sams_colours
print(same_colours)

# The key takeaway from this is that if you're trying to figure out unique elements
# in common between two groups or looking to combine groups to find unique elements,
# sets are a really handy data structure to help you accomplish this.
