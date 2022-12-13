def singleTargetIdentify(l, t):
    out = []
    current = []
    for i in l:
        if i[1] == t:
            current.append(i)
        else:
            out.append(current)
            current = []
    return [i for i in out if len(i) > 0]

def multipleTargetIdentify(l, ts):
    out = []
    current = []
    for i in l:
        if i[1] in ts:
            current.append(i)
        else:
            out.append(current)
            current = []
    return [i for i in out if len(i) > 0]

def number(l):
    return [(l[x], x) for x in range(len(l))]

# Wrote this code while listening to Dragostea Din Tei, can't guarantee functionality. Ck9k
class Table:
    def __init__(self, content):
        # Content should be dictionary of dictionaries

        assert type(content) == dict, "\"content\" argument of Table should be a dictionary of dictionaries"

        keys = None
        for key in content.keys():
            if type(content[key]) != dict:
                raise SyntaxError("\"content\" argument of Table should be a dictionary of dictionaries")

            if keys == None:
                keys = content[key].keys()
            else:
                if content[key].keys() != keys:
                    raise SyntaxError("sub-dictionaries of \"content\" argument of Table should have same list of keys")

        self.content = content

    def get(self, row, col):
        return self.content[row][col]

    def getCol(self, col):
        return [self.content[row][col] for row in self.content.keys()]

    def getRow(self, row):
        return self.content[row]

    def searchRowByColumn(self, col, value):
        for row in self.content.keys():
            if type(row[col]) == type(lambda: None):
                if value.__code__.co_code == row[col].__code__.co_code:
                    return row
            elif row[col] == value:
                return row

        return None
