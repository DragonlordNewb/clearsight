class Node:
    def __init__(self, name):
        self.name = name
        self.tentativeDistance = 0

class Edge:
    def __init__(self, startpoint, endpoint):
        self.startpoint = startpoint
        self.endpoint = endpoint 
    
    def traverse(self, sp=None):
        if sp == None:
            return self.endpoint
        elif sp == self.startpoint:
            return self.endpoint 
        elif sp == self.endpoint:
            return self.startpoint
        else:
            return self.endpoint

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes 
        self.edges = edges

    def __getitem__(self, name):
        for node in self.nodes:
            if node.name == name:
                return node