list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list)
# zip is used to iterate through multiple lists
for x, y in zip(list1, list2):
    print(x, y)

# new variable list3 points to the same list object as list1 in memory. thus when either list1
# or list3 are changed as below, both variables will change as they point to the same object
list3 = list1
print(list1)
print(list3)

# extend appends a whole list on to another list
list3.extend(list2)
print(list3)
print(list1)

# to extend lists without affecting the existing variable, can add as below
list4 = list1 + list2
print(list4)

# alternatively can create a copy of a list which is a new identical list object as below.
# e.g. in below, when changes are made to either list4 or list5, the other list will not be
# affected as it is a copy (the variables point to different list objects)
list5 = list(list4)
