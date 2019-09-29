# String Formatting using .format method

# can leave {} plaeholders empty if want to do in chronological order
s = 'We love {0} {1}'
s1 = s.format('data', 'analysis')

print(s1)

s = 'We love {1} {0}'
s1 = s.format('booties', 'big')

print(s1)
