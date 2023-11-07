text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
question = 'What are vegetables?'


import nltk
nltk.download('wordnet')


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


# Tokenizing sentences
nltk.download('punkt')


def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas


sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)
print(sentence_tokens)
# ['Originally, vegetables were collected from the wild by hunter-gatherers.',
#  'Vegetables are all plants.',
#  'Vegetables can be eaten either raw or cooked.',
#  'What are vegetables?']


from sklearn.feature_extraction.text import TfidfVectorizer


tv = TfidfVectorizer(tokenizer=lemma_me)
print(tv)
# TfidfVectorizer(tokenizer=<function lemma_me at 0x7f31a2caf9e0>)


nltk.download('averaged_perceptron_tagger')


tf = tv.fit_transform(sentence_tokens)
print(tf)
# <4x8 sparse matrix of type '<class 'numpy.float64'>'
	# with 14 stored elements in Compressed Sparse Row format>

tf.toarray()
# array([[0.27717414, 0.53114624, 0.        , 0.        , 0.53114624,
#         0.53114624, 0.        , 0.27717414],
#        [0.41988018, 0.        , 0.        , 0.        , 0.        ,
#         0.        , 0.8046125 , 0.41988018],
#        [0.32713399, 0.        , 0.62688384, 0.62688384, 0.        ,
#         0.        , 0.        , 0.32713399],
#        [0.70710678, 0.        , 0.        , 0.        , 0.        ,
#         0.        , 0.        , 0.70710678]])


import pandas
df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names_out())
print(df)


from sklearn.metrics.pairwise import cosine_similarity
values = cosine_similarity(tf[-1], tf)
print(values)
# array([[0.39198343, 0.59380024, 0.46263733, 1.        ]])


text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
question = 'What are vegetables?' 


index = values.argsort()[0][-2]
print(index)
# 1


values_flat = values.flatten()
print(values_flat)
# array([0.39198343, 0.59380024, 0.46263733, 1.        ])


values_flat.sort()
print(values_flat)
# array([0.39198343, 0.46263733, 0.59380024, 1.        ])


coeff = values_flat[-2]
print(coeff)
# 0.593800244493221


if coeff > 0.3:
    print(sentence_tokens[index])
# Vegetables are all plants.
