import nltk
nltk.download('wordnet')


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

lemma1 = lemmatizer.lemmatize('vegetables', 'n')
lemma2 = lemmatizer.lemmatize('vegetable', 'v')

print(lemma1)
