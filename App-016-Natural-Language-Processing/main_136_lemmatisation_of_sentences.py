import nltk
nltk.download('wordnet')


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
sentence = 'Vegetables are types of plants.'


# Tokenizing sentences

nltk.download('punkt')


sentence_tokens = nltk.word_tokenize(sentence.lower())
print(sentence_tokens)
# ['vegetables', 'are', 'types', 'of', 'plants', '.']


import nltk
nltk.download('averaged_perceptron_tagger')


pos_tags = nltk.pos_tag(sentence_tokens)
print(pos_tags)
# [('vegetables', 'NNS'),
#  ('are', 'VBP'),
#  ('types', 'NNS'),
#  ('of', 'IN'),
#  ('plants', 'NNS'),
#  ('.', '.')]


import nltk

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas


l1 = lemma_me('Vegetables are types of plants.')
print(l1)
# ['vegetable', 'be', 'type', 'plant']


l2 = lemma_me('A vegetable is a type of plant')
print(l2)
# ['vegetable', 'be', 'type', 'plant']


print(l1 == l2)
# True
