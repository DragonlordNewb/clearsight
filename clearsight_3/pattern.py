import nltk

UNKNOWN = "UNKNOWN"

class PatternComponent:
    def __init__(self, *data):
        self.data = data
        self.length = len(self.data)

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        d = self.data + other.data
        return PatternComponent(*d)

    def __sub__(self, other):
        return PatternComponent(*[x for x in self.data if x not in other.data])

    def __len__(self):
        return self.length

    def difference(self, other):
        return len(self - other)

    def similarity(self, other):
        return 1 / self.difference(other)

class Pattern:
    def __init__(self, *data):
        self.data = data
        self.length = len(self.data)
        self.lengths = [len(d) for d in self.data]
        self.metalength = sum(self.lengths)

    def __str__(self):
        return "\n".join([str(x) for x in self.data])

    def __add__(self, other):
        d = self.data + other.data
        return Pattern(*d)

    def __sub__(self, other):
        return Pattern(*[x for x in self.data if x not in other.data])

    def __len__(self):
        return self.length

    def difference(self, other):
        assert self.length == other.length

        diff = 0

        for index in range(self.length):
            diff += max([
                self.data[index].difference(other.data[index]),
                other.data[index].difference(self.data[index])
            ])

        return diff

    def similarity(self, other):
        return 1 / self.difference(other)

class PatternFramework(Pattern):
    def __init__(self, *data):
        Pattern.__init__(self, *data)
        self.knowns = [x for x in self.data if x not in [UNKNOWN, None]]
        self.unknownIndices = [
            x for x in range(self.length) if self.data[x] in [UNKNOWN, None]
        ]

    def __sub__(self, other):
        return Pattern(*[x for x in self.knowns if x not in other.data])

    def fill(self, index, data):
        self.data[index] = data
        self.knowns.append(data)
        self.unknownIndices = [x for x in self.unknownIndices if x != index]

    def inherit(self, patterndata):
        for index in range(self.length):
            if self.data[index] in [UNKNOWN, None]:
                self.fill(index, patterndata.data[index])

    def convert(self):
        return Pattern(*self.data)

class PatternIntelligence:
    def __init__(self, patterns, name=None, selfImprove=False):
        self.patterns = patterns
        self.name = name
        self.selfImprove = selfImprove
        self.history = []

    def add(self, *patterns):
        for pattern in patterns:
            self.patterns.append(pattern)

    def generateCorrectedDatabase(self, indexBlacklist, maximum):
        # Generate a database of all patterns in the set that have the component
        # of the selected index (or indices) removed. Used later in the .fill()
        # function and also helps for matching with frameworks.

        output = []
        for pattern in self.patterns:
            data = []
            for index in range(len(pattern)):
                if (index not in indexBlacklist) and (index <= maximum):
                    data.append(pattern.data[index])
            output.append(Pattern(*data))

        return output

    def match(self, targetPattern): # Low generativity
        # Find the pattern in the existing database that best matches the target
        # pattern and return it. No generativity since the output had to be
        # inserted into the database prior to the .match() call before it could
        # be returned.

        diffs = {}

        for pattern in self.patterns:
            diffs[targetPattern.difference(pattern)] = pattern

        self.history.append((targetPattern, diffs[min(diffs.keys())]))

        return diffs[min(diffs.keys())]

    def fill(self, framework): # Medium generativity
        # Fill in holes in a framework based on existing data and the
        # intelligence's database, then return a pattern converted from that
        # framework using the .convert() method (see above). Medium generativity
        # since the resultant pattern uses existing pattern components, but
        # didn't necessarily exist as a whole before the .fill() call; that is,
        # a new pattern is created from existing components.

        data = []
        for index in range(len(framework.data)):
            database = self.generateCorrectedDatabase(
                framework.unknownIndices, index
            )
            difflist = [(framework.difference(p), p) for p in database]
            # We don't need to fill in the data if it already exists
            if framework.data[index] not in ["UNKNOWN", None]:
                data.append(framework.data[index])
                continue

            framework.inherit(difflist[min(difflist.keys())])

        return framework.convert()

    def make(self, charge): # High generativity
        # Generate a new (pseudo-random) pattern that matches the existing
        # database (or some subset of it) to a decent extent. More complicated
        # due to the higher requirement of parameters. Very generative since
        # although the pattern is based off another existing one, no component
        # of it existed before the .make() call; that is, a new pattern is
        # created from nothing.

        pass

class PatternSuperintelligence:
    def __init__(self, intelligences):
        self.intelligences = intelligences
        
    def select(self, name):
        return [x for x in self.intelligences if x.name == name][0]

    def match(self, targetPattern):
        # Returns a pair (match, name of intelligence that produced it)
        matches = {}
        for intelligence in self.intelligences:
            m = intelligence.match(targetPattern)
            matches[targetPattern.difference(m)] = (m, intelligence.name)
        return matches[min(matches.keys())]

    def fill(self, framework):
        # Convert the framework and match it to find out which intelligence works
        # with it best, then use that one to fill it
        mr = self.match(framework.convert())
        intelligence = self.select(mr[1])
        return intelligence.fill(framework)

    def make(self, charge):
        pass

def unittest_numericalMatching():
    # Numerical matching unit test
    print("[clearsight_3.pattern] Loading unit test for pattern matching ...")

    # Patterns A, B, C, D, and E are test patterns, each with simple data.
    # They are used to "train" the intelligence; more accurately, to add to its
    # database of known patterns.

    A = Pattern(PatternComponent(1), PatternComponent(2), PatternComponent(3))
    B = Pattern(PatternComponent(3), PatternComponent(2), PatternComponent(1))
    C = Pattern(PatternComponent(1), PatternComponent(1), PatternComponent(1))
    D = Pattern(PatternComponent(2), PatternComponent(2), PatternComponent(2))
    E = Pattern(PatternComponent(3), PatternComponent(3), PatternComponent(3))

    # Patterns X, Y, and Z correspond roughly to the test patterns, varying by
    # 0.1 or 0.2 each time. Despite this, the intelligence is able to match the 
    # patterns to their corresponding values in the test pattern database without
    # the use of rounding, which proves its pattern matching capability.

    X = Pattern(PatternComponent(2), PatternComponent(1.9), PatternComponent(2.1))
    # matches D

    Y = Pattern(PatternComponent(1.1), PatternComponent(2), PatternComponent(3))
    # matches A
    
    Z = Pattern(PatternComponent(3), PatternComponent(2), PatternComponent(0.9))
    # matches B

    intelligence = PatternIntelligence([A, B, C, D, E])

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
    
    A = Pattern(
        PatternComponent(*nltk.word_tokenize("Hello, how are you doing?")),
        PatternComponent(*nltk.word_tokenize("I\'m alright, thank you."))
    )
    B = Pattern(
        PatternComponent(*nltk.word_tokenize("Would you like a sandwich?")),
        PatternComponent(*nltk.word_tokenize("Yes, please, thank you."))
    )
    C = Pattern(
        PatternComponent(*nltk.word_tokenize("Can I get a sandwich?")),
        PatternComponent(*nltk.word_tokenize("Yes, one second please."))
    )
    D = Pattern(
        PatternComponent(*nltk.word_tokenize("Thank you for the sandwich.")),
        PatternComponent(*nltk.word_tokenize("Of course, my pleasure."))
    )
    E = Pattern(
        PatternComponent(*nltk.word_tokenize("I have to go, goodbye.")),
        PatternComponent(*nltk.word_tokenize("Alright, goodbye, see you later."))
    )

    # Patterns X, Y, and Z are rough correspondents, like before.

    X = Pattern(
        PatternComponent(*nltk.word_tokenize("May I have a sandwich?")),
        PatternComponent(*nltk.word_tokenize("Yes, one second."))
    )
    # corresponds to C

    Y = Pattern(
        PatternComponent(*nltk.word_tokenize("Do you want a sandwich?")),
        PatternComponent(*nltk.word_tokenize("Yes, please, thanks."))
    )
    # corresponds to B

    Z = Pattern(
        PatternComponent(*nltk.word_tokenize("I've got to go, goodbye.")),
        PatternComponent(*nltk.word_tokenize("Alright, see you later, goodbye."))
    )
    # corresponds to E

    intelligence = PatternIntelligence([A, B, C, D, E])

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