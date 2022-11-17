from clearsight_2.neocortex import memory

def feed(string):
    memory.commit("MAIN", string)
    return "..."
