from blessed import Terminal

from clearsight_1 import neocortex
from clearsight_1 import system

term = Terminal()

def initialize():
    print(term.clear())
    print("".join(["\n" for x in range(term.height)]))

    print("Clearsight-1 Artificial General Intelligence System")
    print("  System version: " + system.specifications.version + " " + system.specifications.release)
    print("  Release number: " + system.specifications.releaseNumber)
    print("Initializing ...")

    print("  Constructing universe ...", end="")
    space = neocortex.unification.Spacefield(dimension=3)
    time = neocortex.unification.Timeline()
    universe = neocortex.unification.Universe(space=space, time=time)
    print("Universe constructed.")

    print("Initialized.")
    print("".join(["_" for _ in range(term.width)]))
    print()
    print("Clearsight-1 application initialized.")
    print("  The intelligence will now respond to user input.")
    print("  Preface an input with \"system command\" to issue a command to the Clearsight-1 system.")
    print()
    while True:
        input_raw = input("<User> ")

        # Check for system commands
        if input_raw[:16].lower() == "system command: ":
            print("<System> System command received: " + str(input_raw[16:]))
            command = input_raw.lower().split(" ")

            if bool(set(["exit", "shutdown", "terminate"]) & set(command)):
                print("  Terminate the Clearsight-1 system? (y/n)")
                while True:
                    with term.cbreak(), term.hidden_cursor():
                        k = term.inkey()
                    if k == "y":
                        print("<System> Shutting down.")
                        print(term.clear())
                        exit()
                    if k == "n":
                        print("<System> Aborting shutdown.")
                        break

        # No system commands; pass the input and respond.
        neocortex.consumption.feed(input_raw)
        print("<Clearsight-1> " + str(neocortex.consumption.extract()))

if __name__ == "__main__":
    initialize()
