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

    print("  Constructing universe ...")

    space = neocortex.unification.Spacefield(dimension=3)
    time = neocortex.unification.Timeline()
    universe = neocortex.unification.Universe(space=space, time=time)

    print("Initialized.")
    print("".join(["_" for _ in range(term.width)]))
    print()
    print("")

if __name__ == "__main__":
    initialize()
