from clearsight_2 import utils

class State:
    def __init__(self, name, resolutionTable, **properties):
        self.properties = properties

        if not type(resolutionTable) == utils.Table:
            raise SyntaxError("invalid state construction: state \"resolutionTable\" must be a utils.Table")

        for condition in resolutionTable.getCol("condition"):
            if type(condition) != type(lambda: None):
                raise SyntaxError("invalid state construction: condition must be a function")

        for callback in resolutionTable.getCol("callback"):
            if type(callback) != type(lambda: None):
                raise SyntaxError("invalid state construction: callback must be a function")

        for resultant in resolutionTable.getCol("resultant"):
            if type(resultant) != State:
                raise SyntaxError("invalid state construction: resultant must be a State")

        self.resolutionTable = resolutionTable

        self.name = name

    def resolve(self):
        for row in self.resolutionTable.keys():
            if self.resolutionTable[row]["condition"](self):
                self.resolutionTable[row]["callback"](self)
                return self.resolutionTable[row]["resultant"]
        
        return self