from clearsight_2.neocortex import memory
from clearsight_2.neocortex.languageprocessing import tokenization

def feed(string):
    memory.commit("MAIN", string)
    tok = tokenization.tokenize(string)
    for tobject in [x[0] for x in tok.objects]:
        if not memory.memoryFileExists(tobject[0]):
            return "What is " + str(tobject[0])
