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
