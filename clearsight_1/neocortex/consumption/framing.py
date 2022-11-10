from clearsight_1.neocortex.languageprocessing import tokenization

output = "..."

syntaxpatterns = ()

def extract():
    global output

    return output

def feed(string):
    global output

    output = tokenization.tokenize(string)
