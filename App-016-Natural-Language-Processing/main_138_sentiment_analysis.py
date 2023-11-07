import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')
nltk.download('twitter_samples')


analyzer = SentimentIntensityAnalyzer()


text1 = 'Hey, what a beautiful day! How amazing it is!'


if analyzer.polarity_scores(text1)['compound'] > 0:
    print('Positive Text')
else:
    print('Negative Text')


len(nltk.corpus.twitter_samples.strings())
# 30000


tweet1 = nltk.corpus.twitter_samples.strings()[1045]
print(tweet1)


scores = analyzer.polarity_scores(tweet1)
print(scores)
