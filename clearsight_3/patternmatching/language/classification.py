from clearsight_3.patternmatching import pattern
from clearsight_3.patternmatching.language import tokenization

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

classifier = pattern.PatternSuperintelligence(None)
