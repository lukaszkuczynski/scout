
# coding: utf-8

# # Get sample data
# Where to start? I have just copied from Wikipedia 4 articles: 2 football players and 2 cars. I think it will be good for matching and comparison.

# In[66]:

car_text_1 = open('testdata/citroen_c4.txt','r', encoding='utf-8').read()
print('First "car" text has %d characters' % len(car_text_1))
print('Sample >> %s' % car_text_1[:100])
car_text_2 = open('testdata/audi_80.txt','r', encoding='utf-8').read()
print('Second "car" text has %d characters' % len(car_text_2))
print('Sample >> %s' % car_text_2[:100])

player_text_1 = open('testdata/citko.txt','r', encoding='utf-8').read()
print('First "player" text has %d characters' % len(player_text_1))
print('Sample >> %s' % player_text_1[:100])
player_text_2 = open('testdata/cantona.txt','r', encoding='utf-8').read()
print('Second "player" text has %d characters' % len(player_text_2))
print('Sample >> %s' % player_text_2[:100])


# Having that fields time for play!

# ## Stopwords
# Remove stop words, there are not a feature of text! Moreover with de-capitalize all words to make them equal.

# In[76]:

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

def text_without_stopwords(input):
    without = [z for z in input.lower().split() if z not in stop]
    return ' '.join(without)

print("Before cleaning:")
print(player_text_1[:100])
print("After:")
player_text_1 = text_without_stopwords(player_text_1)
print(player_text_1[:100])

player_text_2 = text_without_stopwords(player_text_2)
car_text_1 = text_without_stopwords(car_text_1)
car_text_2 = text_without_stopwords(car_text_2)


# ## Time for normalizing
# Now we may want to remove all endings and remove punctuation. This will make text one long text, easier to vectorize.

# In[ ]:
import nltk
stemmer = nltk.stem.porter.PorterStemmer()
print(stemmer.stem("retired"))
print(stemmer.stem("frequently"))


# So this is how stemming works. Now let's apply it to whole text

# In[84]:

import string
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.translate(remove_punctuation_map)))
print(normalize(player_text_1)[:20])


# # Cosine similarity
# `normalize` function will be used now, we will now convert our texts into vectors and compare them using cosine similarity. Then there is going to be short test are we able to MachineLearning way to deduct which are "cars" vs "players".

# In[93]:

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(tokenizer=normalize)

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

print('Player Citko vs Player Cantona = %.3f ' % cosine_sim(player_text_2, player_text_1))
print('Car Citronen vs Player Citko = %.3f ' % cosine_sim(car_text_1, player_text_1))
print('Car Audi vs Player Citko = %.3f' % cosine_sim(car_text_2, player_text_1))
print('Cars are similar! %.3f ' % cosine_sim(car_text_1, car_text_2))


# # Summary
# Voila. Cars had greater similarity between each other in "same" group. The same with football players. So we can tell how we measure text similarity in simple way!
