from string import punctuation

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np


def cleanData(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words('english')
    stop_words.append('’')
    text = text.lower()
    text = ''.join(c for c in text if not c.isdigit())
    text = ''.join(c for c in text if c not in punctuation)
    text = ' '.join([w for w in nltk.word_tokenize(text) if w not in stop_words])
    text = [wordnet_lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text)]
    text = " ".join(w for w in text)
    return text

# fake_news = pd.read_csv('Fake.csv')
# true_news = pd.read_csv('True.csv')
#
# fake_news['label'] = 0
# true_news['label'] = 1
#
# news = pd.concat([fake_news, true_news])
# news = news.reset_index(drop=True)
#
# news_title = news.drop(['subject', 'date', 'text'], axis=1)
# news_text = news.drop(['subject', 'date','title'], axis=1)
#
# news_title = shuffle(news_title, random_state=275035)
# news_text = shuffle(news_text, random_state=275035)
#
# news_title['title'] = news_title['title'].apply(cleanData)
# news_title.to_csv('title_data.csv')
#
# news_text['text'] = news_text['text'].apply(cleanData)
# news_text.to_csv('text_data.csv')


news = pd.read_csv('title_data.csv')
# news = pd.read_csv('text_data.csv')
news = news.dropna()

x_news = news['title']

# x_news = news['text']
y_news = news['label']


tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(x_news)

x_train, x_test, y_train, y_test = train_test_split(tfidf_matrix, y_news, test_size=0.3, random_state=275035)

names = ["Decision tree", "Linear regression", "Naive Bayes", "K-Neighbors", "Passive-Aggressive", "Linear SVC",
         "Random Forest"]
classifiers = [DecisionTreeClassifier(), LogisticRegression(), MultinomialNB(), KNeighborsClassifier(),
               PassiveAggressiveClassifier(max_iter=100), LinearSVC(C=10),
               RandomForestClassifier(n_estimators=10, max_features=2)]

for name, classifier in zip(names, classifiers):
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    Accuracy = accuracy_score(y_test, y_pred)
    print(name)
    print(f'{round(Accuracy * 100, 2)}%')
    print(pd.DataFrame(confusion_matrix(y_test, y_pred), columns=['Fake', 'Real'], index=['Fake', 'Real']))

# mask = np.array(Image.open("us_mask.jpg"))
# real = news[news['label'] == 1]
# real = ''.join([text for text in real.title])
# wordcloud = WordCloud(width=1000, height=1000, max_words=800, mask=mask,
#                       colormap='Blues', background_color='white').generate(real)
#
# plt.figure(figsize=(8, 6))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
#
# fakes = news[news['label'] == 0]
# fakes = ''.join([text for text in fakes.title])
# wordcloud = WordCloud(width=1000, height=1000, max_words=800, mask=mask,
#                       colormap='Reds', background_color='white').generate(fakes)
#
# plt.figure(figsize=(8, 6))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
