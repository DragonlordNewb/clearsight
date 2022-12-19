from clearsight_3.states import states
from clearsight_3.interface import cli

class Superior(State):
    def __init__(self):
        State.__init__(self, "superior", 999)
    
    def run(self):
        global states.currentState
        
        