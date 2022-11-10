from nltk import word_tokenize
from nltk import pos_tag

def tokenize(string):
    # Use an averaged perceptron tagger and other resources to tag the string
    return pos_tag(word_tokenize(string))
