import json
import os

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
