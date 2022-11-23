class Resolution:
    def __init__(self, condition, resultant, properties, weight=0):
        if type(condition) != type(lambda: None):
            raise SyntaxError("Resolution condition must be a function")
        self.condition = condition 

        if type(resultant) != Resolution:
            raise SyntaxError("Resolution resultant must be a Decision")
        self.resultant = resultant 

        if type(properties) != dict:
            raise SyntaxError("Resolution properties must be a dictionary")
        self.properties = properties

        weight = 0

    def getResultant(self):
        out = self.resultant
        out.properties = self.properties
        return out

class Decision:
    def __init__(self, resolutions, **properties):
        self.resolutions = resolutions
        self.properties = properties

    def resolve(self):
        for resolution in self.resolutions:
            if resolution.condition(self):
                return resolution.getResultant()
        
        return self

class WeightedDecisionTree:
    def __init__(self, initialDecision, targetDecision, decisions):
        self.initialDecision = initialDecision
        self.targetDecision = targetDecision
        self.decisions = decisions