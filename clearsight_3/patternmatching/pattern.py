import nltk

UNKNOWN = "UNKNOWN"

class PatternComponent:
    # Basically a fancy list that supports cool math.

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
    # Represents an ordered list of datasets.

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
    # A "partial" pattern; that is, one that can be filled (see PatternIntelligence).
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
    # A god class that creates the most useful object in the module.
    # Allows the procedural, non-deterministic classification of data and
    # pattern matching and filling (guessing incomplete data from existing points).

    def __init__(self, patterns, name=None, selfImprove=False):
        self.patterns = patterns
        self.name = name
        self.selfImprove = selfImprove
        self.history = []

    def add(self, *patterns):
        for pattern in patterns:
            self.patterns.append(pattern)

    def remove(self, *patterns):
        self.patterns = [x for x in self.patterns if x not in patterns]

    def feedback(self, historyIndex, feedback):
        if feedback:
            self.add(self.history[historyIndex][1])
        else:
            self.remove(self.history[historyIndex][0])

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
    # Functionally similar to the PatternIntelligence class, but utilizes several
    # of them as subsystems to be able to categorize, match, and fill many different
    # types of input.

    def __init__(self, intelligences):
        self.intelligences = intelligences
        self.history = []

    def select(self, name):
        return [x for x in self.intelligences if x.name == name][0]

    def feedback(self, historyIndex, feedback):
        intelligence = self.select(self.history[historyIndex][0])
        if feedback:
            intelligence.add(self.history[historyIndex][2])
        else:
            intelligence.remove(self.history[historyIndex][1])

    def match(self, targetPattern):
        # Returns a pair (match, name of intelligence that produced it)
        matches = {}
        for intelligence in self.intelligences:
            m = intelligence.match(targetPattern)
            matches[targetPattern.difference(m)] = (m, intelligence.name)
        self.history.append((
            intelligence.name, targetPattern, matches[min(matches.keys())]
        ))
        return (intelligence.name, matches[min(matches.keys())])

    def fill(self, framework):
        # Convert the framework and match it to find out which intelligence works
        # with it best, then use that one to fill it
        mr = self.match(framework.convert())
        intelligence = self.select(mr[1])
        return intelligence.fill(framework)

    def make(self, charge):
        pass
