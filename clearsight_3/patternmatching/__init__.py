from clearsight_3.patternmatching import language
from clearsight_3.patternmatching import pattern

import nltk

def unittest_numericalMatching():
    # Numerical matching unit test
    print("[clearsight_3.pattern] Loading unit test for pattern matching ...")

    # pattern.Patterns A, B, C, D, and E are test patterns, each with simple data.
    # They are used to "train" the intelligence; more accurately, to add to its
    # database of known patterns.

    A = pattern.Pattern(pattern.PatternComponent(1), pattern.PatternComponent(2), pattern.PatternComponent(3))
    B = pattern.Pattern(pattern.PatternComponent(3), pattern.PatternComponent(2), pattern.PatternComponent(1))
    C = pattern.Pattern(pattern.PatternComponent(1), pattern.PatternComponent(1), pattern.PatternComponent(1))
    D = pattern.Pattern(pattern.PatternComponent(2), pattern.PatternComponent(2), pattern.PatternComponent(2))
    E = pattern.Pattern(pattern.PatternComponent(3), pattern.PatternComponent(3), pattern.PatternComponent(3))

    # pattern.Patterns X, Y, and Z correspond roughly to the test patterns, varying by
    # 0.1 or 0.2 each time. Despite this, the intelligence is able to match the
    # patterns to their corresponding values in the test pattern database without
    # the use of rounding, which proves its pattern matching capability.

    X = pattern.Pattern(pattern.PatternComponent(2), pattern.PatternComponent(1.9), pattern.PatternComponent(2.1))
    # matches D

    Y = pattern.Pattern(pattern.PatternComponent(1.1), pattern.PatternComponent(2), pattern.PatternComponent(3))
    # matches A

    Z = pattern.Pattern(pattern.PatternComponent(3), pattern.PatternComponent(2), pattern.PatternComponent(0.9))
    # matches B

    intelligence = pattern.PatternIntelligence([A, B, C, D, E])

    print("[clearsight_3.pattern] Loaded, starting unit test ...")

    mX = intelligence.match(X)
    qX = mX == D
    print("  (intelligence.match(X) == D) == " + str(qX))

    mY = intelligence.match(Y)
    qY = mY == A
    print("  (intelligence.match(Y) == A) == " + str(qY))

    mZ = intelligence.match(Z)
    qZ = mZ == B
    print("  (intelligence.match(Z) == B) == " + str(qZ))

    out = qX and qY and qZ
    print("  (qX and qY and qZ) == " + str(out))
    assert out, "Unit test failure"
    print("[clearsight_3.pattern] Unit test passed.")
    return True

def unittest_naturalLanguageMatching_1():
    # Natural language matching test - for typo correction & the like

    print("[clearsight_3.pattern] Loading unit test for NL matching ...")

    # Like before, A, B, C, D, and E are all training patterns. They're added
    # to the database of the intelligence so that it can match the test patterns.

    A = pattern.Pattern(
        pattern.PatternComponent(*nltk.word_tokenize("Hello, how are you doing?")),
        pattern.PatternComponent(*nltk.word_tokenize("I\'m alright, thank you."))
    )
    B = pattern.Pattern(
        pattern.PatternComponent(*nltk.word_tokenize("Would you like a sandwich?")),
        pattern.PatternComponent(*nltk.word_tokenize("Yes, please, thank you."))
    )
    C = pattern.Pattern(
        pattern.PatternComponent(*nltk.word_tokenize("Can I get a sandwich?")),
        pattern.PatternComponent(*nltk.word_tokenize("Yes, one second please."))
    )
    D = pattern.Pattern(
        pattern.PatternComponent(*nltk.word_tokenize("Thank you for the sandwich.")),
        pattern.PatternComponent(*nltk.word_tokenize("Of course, my pleasure."))
    )
    E = pattern.Pattern(
        pattern.PatternComponent(*nltk.word_tokenize("I have to go, goodbye.")),
        pattern.PatternComponent(*nltk.word_tokenize("Alright, goodbye, see you later."))
    )

    # pattern.Patterns X, Y, and Z are rough correspondents, like before.

    X = pattern.Pattern(
        pattern.PatternComponent(*nltk.word_tokenize("May I have a sandwich?")),
        pattern.PatternComponent(*nltk.word_tokenize("Yes, one second."))
    )
    # corresponds to C

    Y = pattern.Pattern(
        pattern.PatternComponent(*nltk.word_tokenize("Do you want a sandwich?")),
        pattern.PatternComponent(*nltk.word_tokenize("Yes, please, thanks."))
    )
    # corresponds to B

    Z = pattern.Pattern(
        pattern.PatternComponent(*nltk.word_tokenize("I've got to go, goodbye.")),
        pattern.PatternComponent(*nltk.word_tokenize("Alright, see you later, goodbye."))
    )
    # corresponds to E

    intelligence = pattern.PatternIntelligence([A, B, C, D, E])

    print("[clearsight_3.pattern] Loaded, starting unit test ...")

    mX = intelligence.match(X)
    qX = mX == C
    print("  (intelligence.match(X) == C) == " + str(qX))

    mY = intelligence.match(Y)
    qY = mY == B
    print("  (intelligence.match(Y) == B) == " + str(qY))

    mZ = intelligence.match(Z)
    qZ = mZ == E
    print("  (intelligence.match(Z) == E) == " + str(qZ))

    out = qX and qY and qZ
    print("  (qX and qY and qZ) == " + str(out))
    assert out, "Unit test failure"
    print("[clearsight_3.pattern] Unit test passed.")
    return True
