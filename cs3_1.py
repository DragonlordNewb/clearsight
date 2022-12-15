import clearsight_3

print("[cs3_1] Loading Clearsight-3-1 Artificial General Intelligence system ...")

properNouns = []

state = clearsight_3.states.WAITING
listeningFor = ""

while True:
    inp = input("<user> ")
    cmd = inp.lower().split(" ")
    if cmd[0] == "$":
        print("<system> Command received.")
        if cmd[1] == "exit":
            exit()

        if cmd[1] == "dump":
            print([str(x) for x in clearsight_3.memory.shortterm.memories])

    output = "..."

    if state == clearsight_3.states.WAITING:
        tk = clearsight_3.patternmatching.language.tokenization.tokenize(inp)
        
        for po in tk.properObjects:
            if po not in properNouns:
                output = "What is " + str(po[0])
                listeningFor = po[0]
                state == clearsight_3.states.LISTENING

    if state == clearsight_3.states.LISTENING:
        clearsight_3.memory.shortterm.write(clearsight_3.unification.Definition(listeningFor, inp))
        state = clearsight_3.states.WAITING

    print("<clearsight> " + output)
