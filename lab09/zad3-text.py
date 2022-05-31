from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer


n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs

nltk.download('vader_lexicon')

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)


trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))


positive = " The hotel felt like home,I was very comfortable and impress with the kind gestures and clean" \
           " environment with a very helpful manager Mr CARTER, he's far too kind. He's always there to assist." \
           " I really enjoyed my stay at Abbey Lodge and I can't wait to visit again. Thank you it was an holiday to" \
           " remember."

negative = "Breakfast was awful we skipped it the second day. The bathroom was clearly newly fitted but they hadn’t" \
           " fitted the taps correctly so when I tried to have a bath the water wouldn’t stop running, I contacted " \
           "the person working there who just panicked and said she’d get her boss to sort it, the boss never came so" \
           " I had a try at fixing it myself, I managed. Good job too as the manager never arrived. I didn’t risk using" \
           " the shower or bath after that though.,"


positive = tokenize.sent_tokenize(positive)

negative = tokenize.sent_tokenize(negative)

for sentence in negative:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()


print("-------------")
for sentence in positive:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()