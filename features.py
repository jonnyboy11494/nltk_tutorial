#sentiment analysis
import nltk
import random
from nltk.corpus import movie_reviews

#documents = [(list(movie_reviews.words(fileid)), category)
#             for category in movie_reviews.categories()
#             for fileid in movie_reviews.fileids(category)]

documents = []
# for positive and negative category
for category in movie_reviews.categories():
    # and each movie in this category
    for fileid in movie_reviews.fileids(category):
        # compile the (words and category) tuple to a "document" list
        documents.append((list(movie_reviews.words(fileid)), category)) #this is a tuple (a list that cannot be changed)

# shuffle all the documents in the list
random.shuffle(documents)

# print(documents[1])

# all lowercase words from movie reviews
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

# frequency distribution of all words
all_words = nltk.FreqDist(all_words)
# 3000 most common words
word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document) #converting a list to a set means that repeating elements are removed (term presence)
    features = {} #empty dictionary
    # features are a dictionary of the top 3000 words and whether they exist or not in the document
    for w in word_features:
        features[w] = (w in words)

    return features

#print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

#featuresets = [(find_features(rev), category) for(rev, category) in documents]
featuresets = []
for (rev, category) in documents:
    featuresets.append((find_features(rev), category))

# print labelled featue set for document 1
print(featuresets[1])

