from clearsight_3.patternmatching import pattern
from clearsight_3.patternmatching.language import tokenization
from clearsight_3 import datasets

import nltk

# c1 = pattern.PatternIntelligence(
#     [pattern.Pattern(pattern.PatternComponent(tokenization.tag(input("1> "))))
#     for x in range(3)],
#     name="c1"
# )
#
# c2 = pattern.PatternIntelligence(
#     [pattern.Pattern(pattern.PatternComponent(tokenization.tag(input("2> "))))
#     for x in range(3)],
#     name="c2"
# )
#
# c3 = pattern.PatternIntelligence(
#     [pattern.Pattern(pattern.PatternComponent(tokenization.tag(input("3> "))))
#     for x in range(3)],
#     name="c3"
# )

questionClassifier = pattern.PatternIntelligence(datasets.questions, "classQ")
statementClassifier = pattern.PatternIntelligence(datasets.questions, "classS")

classifier = pattern.PatternSuperintelligence(None)
