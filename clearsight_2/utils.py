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