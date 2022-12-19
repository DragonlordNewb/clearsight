# a state machine! gotta love em.
# navigates states based on a "charge" value, always moving from lowest-charge to highest.
# uses Dijkstra's algorithm to determine the path between states.

currentState = None

class State:
    def __init__(self, name, charge):
        self.name = name
        self.charge = charge

    def run(self):
        raise RuntimeError("Cannot run the blank state, the \"run\" method must be overridden by a daughter class.")