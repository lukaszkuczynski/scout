import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer




# So this is how stemming works. Now let's apply it to whole text

# In[84]:


def stem_tokens(tokens):
    stemmer = nltk.stem.porter.PorterStemmer()
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    return stem_tokens(nltk.word_tokenize(text.translate(remove_punctuation_map)))


class SimilarityCalculator:


    def __init__(self, threshold=0.1):
        self.threshold = threshold
        self.vectorizer = TfidfVectorizer(tokenizer=normalize)

    def cosine_sim(self, text1, text2):
        tfidf = self.vectorizer.fit_transform([text1, text2])
        value = ((tfidf * tfidf.T).A)[0, 1]
        # print(f"Cosine similarity is {value}")
        return value

    def are_similar(self, text1, text2):
        return self.cosine_sim(text1, text2) > self.threshold

