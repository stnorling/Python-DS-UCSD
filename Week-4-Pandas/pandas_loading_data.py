import pandas as pd
##################### Loading data in to Pandas #####################

# below, movies is a pandas DataFrame type object. using the .read_csv
# method we pass in arguments for file and seperator
movies = pd.read_csv('./movielens/movies.csv', sep=',')
print(type(movies))

# .head is a DataFrame method that displays the first 5 rows by 
# default. We can pass in a different number to get back
# a different number of rows of data, e.g. .head(15)
print(movies.head())

tags = pd.read_csv('./movielens/tags.csv', sep=',')
print(tags.head())

ratings = pd.read_csv('./movielens/ratings.csv', sep=',', 
                      parse_dates=['timestamp'])
print(ratings.head())
# ADD NOTES ABOUT PARSE_DATES ##############
ratings = pd.read_csv('./movielens/ratings.csv', sep=',', 
                      parse_dates=['timestamp'])
print(ratings.head())