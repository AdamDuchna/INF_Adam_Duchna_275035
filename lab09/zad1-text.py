import nltk
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from wordcloud import WordCloud

news = open("taiwan-news.txt",'r')
news = news.read()
news = nltk.word_tokenize(news)

stopwords = nltk.corpus.stopwords.words("english")


news = [w for w in news if w.lower() not in stopwords]

print(news)

stopwords.append('.')
stopwords.append('``')
stopwords.append("''")
stopwords.append('-')
stopwords.append(',')
stopwords.append("'s")
stopwords.append("'")
stopwords.append("(")
stopwords.append(")")


news = [w for w in news if w.lower() not in stopwords]

print(len(news))

lemmatizer = WordNetLemmatizer()

news = [lemmatizer.lemmatize(w) for w in news ]

print(len(news))

fdist = FreqDist(news)
print(fdist)

fdist.plot(10,cumulative=False)
plt.show()

wc = WordCloud(max_words=277, margin=5,
               random_state=1).generate(news)

default_colors = wc.to_array()
plt.imshow(wc,
           interpolation="bilinear")