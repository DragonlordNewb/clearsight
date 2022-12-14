import clearsight_3

print("[cs3_1] Loading Clearsight-3-1 Artificial General Intelligence system ...")

while True:
    inp = input("<user> ")
    cmd = inp.lower().split(" ")
    if cmd[0] == "$":
        print("<system> Command received.")
        if cmd[1] == "exit":
            exit()
    tk = clearsight_3.patternmatching.language.tokenization.tokenize(inp)

    output = "..."

    print("<clearsight> " + output)
