import nltk
import numpy as np
from string import punctuation
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def cleaner(text):
    text = text.lower()

    text = ''.join(c for c in text if not c.isdigit())
    text = ''.join(c for c in text if c not in punctuation)

    stopwords = nltk.corpus.stopwords.words("english")
    text = ' '.join([w for w in nltk.word_tokenize(text) if not w in stopwords])

    wordnet_lemmatizer = WordNetLemmatizer()
    text = [wordnet_lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text)]

    text = " ".join(w for w in text)
    return text


vectorizer = CountVectorizer()

testData = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
testData = [cleaner(w) for w in testData]
tdif = TfidfVectorizer()
X = vectorizer.fit_transform(testData)
X2 = tdif.fit_transform(testData)

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

df2 = pd.DataFrame(X2.toarray(), columns=vectorizer.get_feature_names_out())


word_list = vectorizer.get_feature_names_out()
count_list = X.toarray().sum(axis=0)

print(df.head())
print(df2.head())
print( dict(zip(word_list,count_list)) )



