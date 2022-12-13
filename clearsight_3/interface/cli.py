import blessed

t = blessed.Terminal()

def initializeCLI():
    print(t.clear())
    

    h = []

    while True:

        for index in range(len(h)):
            with t.location(0, t.height - index):
                print(h[index])
        
        with t.location(0, 0):
            print(t.center("Clearsight-3 Artificial General Intelligence System"))

        with t.location(0, t.height):
            h.append(input("> "))
        print(t.clear())

