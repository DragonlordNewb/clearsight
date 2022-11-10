from difflib import SequenceMatcher

class MatchingData:
	def __init__(self, **data):
		self.data = data

	def checkSimilarity(self, otherMatchingData):
		if not self.isCompatible(otherMatchingData):
			raise TypeError("Cannot check similarity between MatchingData and " + str(otherMatchingData.__name__))

		similarity = []
		for key in self.data.keys():
			if type(self.data[key]) == type(otherMatchingData.data[key]) == str:
				sm = SequenceMatcher(None, self.data[key], otherMatchingData.data[key])
				ratio = sm.ratio()
				similarity.append(ratio)

			elif type(self.data[key]) == type(otherMatchingData.data[key]) == int:
				difference = otherMatchingData.data[key] - self.data[key]
				if difference != 0:
					similarity = difference / (0.5 * self.data[key] * otherMatchingData[key])
				similarity.append(similarity)

		return sum(similarity)

	def isCompatible(self, otherMatchingData):
		if isinstance(otherMatchingData, MatchingData):
			return self.data.keys() == otherMatchingData.data.keys()
		return False

class PatternMatcher:
	def __init__(self, datamap):
		self.datamap = {}

		for key in datamap.keys():
			if len(self.datamap.keys()) == 0:
				self.datamap[key] = datamap[key]
			else:
				if not self.isCompatible(datamap[key]):
					raise TypeError("Incompatible MatchingData.")
				self.datamap[key] = datamap[key]

	def isCompatible(self, data):
		return self.datamap[self.datamap.keys()[0]].isCompatible(data)

	def add(self, key, value):
		if self.isCompatible(value):
			self.datamap[key] = value

	def matchOutput(self, keyData):
		similarityMatch = {}
		for key in self.data.keys():
			similarityMatch[key] = keyData.checkSimilarity(self.data[key])
		for key in similarityMatch.keys():
			pass
