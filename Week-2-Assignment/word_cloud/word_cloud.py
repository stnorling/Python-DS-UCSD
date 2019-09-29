# Below task is to create a data structure to store the words and the number of
# occurrences of the words in the text text of A Tale of Two Cities, by Charles Dickens.
# Each word is read in from a file, made it lower case and removing punctuation.
# Common words are skipped by checking if the words exist in the set 'stopwords'.
# For each remaining word, the word is added to the dictionary and count updated for
# that word. The top 10 most frequent words are then extracted from the dictionary
# and printed along with their frequencies.

import string

fh = open('98-0.txt', encoding="utf8")

# stopwords contains common words we do not wish to count
stopwords = set(line.strip() for line in open('stopwords'))
wordcount = dict()
# print(type(stopwords))
garbage = string.punctuation + "“"
# print(garbage)

for line in fh:
    line = line.strip().lower().translate(line.maketrans('','',garbage))
    words = line.split()
    for word in words:
        if word not in stopwords:
            wordcount[word] = wordcount.get(word, 0) + 1

mlist = list()

for k, v in wordcount.items():
    mlist.append((v, k))

mlist.sort(reverse = True)
for v, k in mlist[:10]:
    print(k, v)

#quit()


###################### Unused provided sample code below ######################

# https://docs.python.org/2/library/collections.html
import collections

# Hint: To eliminate duplicates, remember to split by punctuation,
# and use case demiliters. The functions lower() and split() will be useful!

for word in file.read().lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.

# below, a collections.Counter object is created
d = collections.Counter(wordcount)
# print(type(d))

# most_common([n]) is a collections.Counter object method that returns a list of the
# n most common elements and their counts from the most common to the least. If n is
# omitted or None, most_common() returns all elements in the counter. Elements with
# equal counts are ordered arbitrarily.

# print(d.most_common(10))
for word, count in d.most_common(10):
	print(word, ": ", count)
