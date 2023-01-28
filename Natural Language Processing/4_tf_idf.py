'''
A) TF = term frequency
no of repetition of words in a sentence
divided by
no of words in a sentence

B) IDF = invert document frequency
log(
    no of sentences
    divided by
    no of sentence containing words
)

C) Example
sent 1: good boy
sent 2: good girl
# sent 3: boy girl good

C.1) TF Table
      s1   s2   s3
good: 1/2  1/2  1/3
boy:  1/2  0    1/3
girl: 0    1/2  1/3

C.2) IDF Table
good: log(3/3) = 0
boy: log(3/2)
girl: log(3/2)

C.3) Net Vector Table = TF * IDF (matrix multiplication)
        good            boy             girl
sent 1: 1/2 * log(3/3)  1/2 * log(3/2)  0 * log(3/2)
sent 2: 1/2 * log(3/3)  0 * log(3/2)    1/2 * log(3/2)
sent 3: 1/2 * log(3/3)  1/3 * log(3/2)  1/3 * log(3/2)
Net=>
        good  boy             girl
sent 1: 0     1/2 * log(3/2)  0
sent 2: 0     0               1/2 * log(3/2)
sent 3: 0     1/3 * log(3/2)  1/3 * log(3/2)

this is net vector table
this tells about a bit more detailed information
about what words are more important in the sentences
'''

import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""

sentences = nltk.sent_tokenize(paragraph)

lm = WordNetLemmatizer()
corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i]).lower().split()
    review = ' '.join([lm.lemmatize(word) for word in review if not word in set(stopwords.words('english'))])
    corpus.append(review)

# creating the bag of words
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=1500)
tfidf.fit(corpus)

x = pd.DataFrame(tfidf.transform(corpus).toarray(), columns = tfidf.get_feature_names_out())
print(x)