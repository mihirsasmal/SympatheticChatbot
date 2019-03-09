#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


# In[5]:


sentiment = pd.read_csv("TwitterDataSet.csv")


# In[6]:


print(sentiment.head())


# In[7]:


print(sentiment['sentiment'].head)


# In[8]:


print(sentiment['sentiment'].value_counts())


# In[9]:


messages= sentiment['content']


# In[10]:


print(messages.head)


# In[11]:


messages = [message for message in messages]
print(messages)


# In[12]:


print(messages[:5])


# In[13]:


def preprocess(document):
   'changes document to lower case and removes stopwords'

   # change sentence to lower case
   document = document.lower()

   # tokenize into words
   words = word_tokenize(document)

   # remove stop words
   words = [word for word in words if word not in stopwords.words("english")]

   # join words to make sentence
   document = " ".join(words)

   return document

#documents = [preprocess(document) for document in documents]
#print(documents)


# In[77]:


messages = [preprocess(message) for message in messages]
print(messages[:6])


# In[79]:


from sklearn.feature_extraction.text import CountVectorizer


# In[80]:


vectorizer = CountVectorizer()
bow_model = vectorizer.fit_transform(messages)
print(bow_model.toarray())


# In[81]:


print(bow_model.shape)
print(vectorizer.get_feature_names())


# In[82]:


from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

# add stemming and lemmatisation in the preprocess function
def preprocess(document, stem=True):
   'changes document to lower case and removes stopwords'

   # change sentence to lower case
   document = document.lower()

   # tokenize into words
   words = word_tokenize(document)

   # remove stop words
   words = [word for word in words if word not in stopwords.words("english")]

   if stem:
       words = [stemmer.stem(word) for word in words]
   else:
       words = [wordnet_lemmatizer.lemmatize(word, pos='v') for word in words]

   # join words to make sentence
   document = " ".join(words)

   return document


# In[83]:


messages = [preprocess(message, stem=False) for message in sentiment.content]

# bag of words model
vectorizer = CountVectorizer()
bow_model = vectorizer.fit_transform(messages)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:


data_set = []
for index,row in sentiment.iterrows():
   data_set.append((row['sentiment'], row['content']))


# In[15]:


print(data_set[:5])


# In[16]:


print(len(data_set))


# In[17]:


stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()


# In[18]:


def preprocess(document, stem=True):
   'changes document to lower case, removes stopwords and lemmatizes/stems the remainder of the sentence'

   # change sentence to lower case
   document = document.lower()

   # tokenize into words
   words = word_tokenize(document)

   # remove stop words
   words = [word for word in words if word not in stopwords.words("english")]

   if stem:
       words = [stemmer.stem(word) for word in words]
   else:
       words = [wordnet_lemmatizer.lemmatize(word, pos='v') for word in words]

   # join words to make sentence
   document = " ".join(words)

   return document


# In[19]:


import nltk
nltk.download('punkt')


# In[20]:


nltk.download('stopwords')


# In[21]:


nltk.download('wordnet')


# In[22]:


messages_set = []
for (message, label) in data_set:
   words_filtered = [e.lower() for e in preprocess(message, stem=False).split() if len(e) >= 3]
   messages_set.append((words_filtered, label))


# In[23]:


print(messages_set[:5])


# In[24]:


print(len(messages_set))


# In[25]:


def get_words_in_messages(messages):
   wordlist=[]
   for (label, message) in messages:
     words = nltk.tokenize.word_tokenize(message)     
     for(word)in words:
      wordlist.append(word)
   return wordlist


# In[26]:


def get_word_features(words):

   
   wordlist = nltk.FreqDist(words)
   word_features = wordlist.keys()
   return word_features


# In[27]:


word_features = get_word_features(get_words_in_messages(messages_set))
print(len(word_features))


# In[28]:


print(word_features)


# In[29]:


sliceIndex = int((len(messages_set)*.8))
random.shuffle(messages_set)


# In[30]:


train_messages, test_messages = messages_set[:sliceIndex], messages_set[sliceIndex:]


# In[31]:


print(len(train_messages))
print(len(test_messages))


# In[32]:


def extract_features(document):
   document_words = set(document)
   features = {}
   for word in word_features:
       features['contains(%s)' % word] = (word in document_words)
   return features


# In[33]:


training_set = nltk.classify.apply_features(extract_features, train_messages)
testing_set = nltk.classify.apply_features(extract_features, test_messages)


# In[34]:


print(training_set[:5])


# In[35]:


print('Training set size : ', len(training_set))
print('Test set size : ', len(testing_set))


# In[2]:


SentimentAnalyzer = nltk.NaiveBayesClassifier.train(training_set)


# In[1]:


print(nltk.classify.accuracy(SentimentAnalyzer, training_set))


# In[267]:


m=test_messages[1009][1]


# In[268]:


print(m)


# In[269]:


SentimentAnalyzer.classify(extract_features(m.split()))


# In[270]:


print


# In[ ]:




