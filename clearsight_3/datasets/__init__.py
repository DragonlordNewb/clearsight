from clearsight_3.patternmatching import pattern
from clearsight_3.patternmatching.language import tokenization

import json
import os
import tqdm

def readFile(filename):
    path = os.getcwd() + "/clearsight_3/datasets/" + filename
    print("[clearsight_3.datasets] Reading file " + str(path) + " ...", end="")
    if os.path.exists(path):
        with open(path, "r") as f:
            output = f.read()
        print("done.")
        return json.loads(output)
    else:
        return FileNotFoundError

def parse(output):
    pass

def parseRaw(filename):
    path = os.getcwd() + "/clearsight_3/datasets/" + filename
    print("[clearsight_3.datasets] Reading file " + str(path) + " ...", end="")
    if os.path.exists(path):
        with open(path, "r") as f:
            output = f.read()
        print("done.")
        out = []
        for line in tqdm.tqdm(output.split("\n"), desc="  Tokenizing data"):
            out.append(tokenization.tokenize(line).convert())
        return out
    else:
        return FileNotFoundError

sandwich_questions = parseRaw("basic/questions/sandwich.rawnlp.dat")
questions = parseRaw("basic/questions/all.json")
statements = parseRaw("basic/statements/all.json")
