from clearsight_2.neocortex import memory
from clearsight_2.neocortex.languageprocessing import tokenization

def feed(string):
    memory.commit("MAIN", string)
    return str(tokenization.tokenize(string))
