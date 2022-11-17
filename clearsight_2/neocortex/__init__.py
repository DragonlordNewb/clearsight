from clearsight_2.neocortex import languageprocessing
from clearsight_2.neocortex import cores
from clearsight_2.neocortex import memory

def feed(string):
    return str(cores.currentCore.feed(string))
