from clearsight_1.neocortex.patternrecognition import mathematical

output = "..."

patterns = {
    "hello world": "Foo bar.",
    "how are you": "I'm good, how are you?",
    "i\'m good": "That's good!",
    "what\'s your name": "I\'m Clearsight-1. What\'s your name?",
    "my name is": "Nice to meet you!"
}

def extract():
    return output

def feed(inp):
    global output

    global patterns

    insplit = inp.split(" ")

    patternsBySimilarity = {}
    for pattern in patterns:
        patternsBySimilarity[pattern] = mathematical.counterCosineSimilarity(insplit, pattern.split(" "))

    for pattern in patternsBySimilarity.keys():
        if patternsBySimilarity[pattern] == max(patternsBySimilarity.values()):
            output = str(patterns[pattern])
            return output
