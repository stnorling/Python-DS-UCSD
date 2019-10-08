import pandas as pd
ser = pd.Series([100, 200, 300, 400, 500], index = ['tom', 'bob', 'nancy', 'dan', 'eric'])

print(ser.loc[['tom', 'bob']])
print(ser[['tom', 'bob']])

# it's possible to index multiple numbers using a rank 2 array
print(ser[[0, 1]])
print(ser.iloc[[0, 1]])

