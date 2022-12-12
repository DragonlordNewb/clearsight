
UNKNOWN = "UNKNOWN"

class PatternComponent:
    def __init__(self, *data):
        self.data = data
        self.length = len(self.data)

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
                self.data[index] - other.data[index],
                other.data[index] - self.data[index]
            ])

        return diff

    def similarity(self, other):
        return 1 / self.difference(other)

class PatternFramework(Pattern):
    def __init__(self, *data):
        Pattern.__init__(self, *data)
        self.knowns = [x for x in self.data if x not in [UNKNOWN, None]]

    def __sub__(self, other):
        return Pattern(*[x for x in self.knowns if x not in other.data])

    def fill(self, index, data):
        self.data[index] = data
        self.knowns.append(data)

    def inherit(self, patterndata):
        for index in range(self.length):
            if self.data[index] in [UNKNOWN, None]:
                self.fill(index, patterndata.data[index])

    def convert(self):
        return Pattern(*self.data)

class PatternIntelligence:
    def __init__(self, patterns):
        self.patterns = patterns

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
            output.apend(Pattern(*data))

    def match(self, targetPattern): # Low generativity
        # Find the pattern in the existing database that best matches the target
        # pattern and return it. No generativity since the output had to be
        # inserted into the database prior to the .match() call before it could
        # be returned.

        diffs = {}

        for pattern in self.patterns:
            diffs[targetPattern.difference(pattern)] = pattern

        return diffs[min(diffs.keys())]

    def fill(self, framework): # Medium generativity
        # Fill in holes in a framework based on existing data and the
        # intelligence's database, then return a pattern converted from that
        # framework using the .convert() method (see above). Medium generativity
        # since the resultant pattern uses existing pattern components, but
        # didn't necessarily exist as a whole before the .fill() call; that is,
        # a new pattern is created from existing components.

        data = []
        for index in framework.data:
            # We don't need to fill in the data if it already exists
            if framework.data[index] not in ["UNKNOWN", None]:
                data.append(framework.data[index])
                continue

            for pattern in self.patterns:
                if pattern.

    def make_stochastic(self, charge): # High generativity
        # Generate a new (pseudo-random) pattern that matches the existing
        # database (or some subset of it) to a decent extent. More complicated
        # due to the higher requirement of parameters. Very generative since
        # although the pattern is based off another existing one, no component
        # of it existed before the .make_stochastic() call; that is, a new
        # pattern is created from nothing.
