from clearsight_2.neocortex import memory
from clearsight_2.neocortex.languageprocessing import tokenization

def feed(string):
    memory.commit("MAIN", string)
    tok = tokenization.tokenize(string)
    for properObject in [x[0] for x in tok.properObjects]:
        if not memory.memoryFileExists(properObject):
            return "q:" + str(properObject)
