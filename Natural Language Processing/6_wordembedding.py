import numpy as np
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, Embedding

reviews = [
    'nice food',
    'amazing restaurant',
    'too good',
    'just loved it',
    'will go again',
    'horrible food',
    'never go there',
    'poor service',
    'poor quality',
    'needs improvement'
]

sentiment = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])


words = ' '.join(
    list(
        set(
            ' '
            .join(reviews)
            .split()
            )
        )
    )
vocab_size = len(words)

words_index = dict()

index = 0
for word in words.split():
    words_index[word] = index
    index += 1
    
words_encoding = one_hot(words, vocab_size)

encoded_reviews = [
    [
        words_encoding[words_index[word]]
        for word in review.split()
    ]
    for review in reviews
]

max_length = 3
padded_reviews = pad_sequences(encoded_reviews, maxlen=max_length, padding='post')

vector_size = 5

model = Sequential()
model.add(
    Embedding(
        vocab_size,
        vector_size,
        input_length=max_length,
        name="embedding"
    )
)
model.add(Flatten())
model.add(Dense(
    1, activation = 'sigmoid'
))

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(
    padded_reviews,
    sentiment,
    epochs = 50,
    verbose = 0
)

model.evaluate(padded_reviews, sentiment)

print(model.get_layer('embedding').get_weights()[0])