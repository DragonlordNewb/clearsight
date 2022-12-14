from clearsight_3.patternmatching.language import tokenization

class Definition:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = tokenization.tokenize(meaning)

    def __contains__(self, other):
        return other in self.meaning or other == word