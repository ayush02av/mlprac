# Movie Review Sentiment Analysis

> To analyse the sentiment as negative or positive for a given movie review text.

Steps
- Find a suitable dataset
- Analyse how to clean the dataset
- Vectorize the text information of reviews
- Perform various ML algorithms

# Dataset Preview

[Dataset Here](https://www.kaggle.com/code/lakshmi25npathi/sentiment-analysis-of-imdb-movie-reviews/input)

Shape (50000, 2)

| **Review** | **Sentiment** |
|:-----------|:--------------|
|`'Phil the Alien is one of those quirky films where the humour is based around the oddness of everything rather than actual punchlines.<br /><br />At first it was very odd and pretty funny but as the movie progressed I didn\'t find the jokes or oddness funny anymore.<br /><br />Its a low budget film (thats never a problem in itself), there were some pretty interesting characters, but eventually I just lost interest.<br /><br />I imagine this film would appeal to a stoner who is currently partaking.<br /><br />For something similar but better try "Brother from another planet"'`|negative|

# Vectorization of dataset

- Used [word2vector](https://radimrehurek.com/gensim/models/word2vec.html) model for creating word embeddings
- Averaged the net vectors of all words for sentence vectors

# Machine Learning

Algorithms used
- Logistic Regression: 85.5%
- Support Vector Machine: 86.9%
- Random Forest: 83.3%
- XGBoost: 85%

Artificial Neural Network
- 1st layer: 50, 2nd layer: 10 :: Training 89.73%, Validation 85.45%
- 60, 20 :: 91.23% 84.36%
- 60, 20, Standard Scaling :: 96.39%, 82.11%
- 0.1 Dropout, 60, 20, :: 85.54%, 85.30%
- 0.1-60, 30, 10 :: 90.11%, 84.61%