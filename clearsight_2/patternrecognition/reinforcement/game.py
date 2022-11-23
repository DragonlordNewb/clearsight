INFINITY = "INFINITY"

def Dijkstra(initialNode, nodes, metric):
    # 1. Mark all nodes unvisited. Create a set of all the unvisited nodes
    #    called the unvisited set.

    unvisited = set()
    for node in nodes:
        unvisited.add(node)

    # 2. Assign to every node a tentative distance value: set it to zero for our
    #    initial node and to infinity for all other nodes. During the run of the
    #    algorithm, the tentative distance of a node v is the length of the
    #    shortest path discovered so far between the node v and the starting
    #    node. Since initially no path is known to any other vertex than the
    #    source itself (which is a path of length zero), all other tentative
    #    distances are initially set to infinity. Set the initial node as
    #    current.

    for node in nodes:
        setattr(node, "tentativeDistance", INFINITY)

    setattr(node, "tentativeDistance", 0)

    # 3. For the current node, consider all of its unvisited neighbors and
    #    calculate their tentative distances through the current node. Compare
    #    the newly calculated tentative distance to the one currently assigned
    #    to the neighbor and assign it the smaller one. For example, if the
    #    current node A is marked with a distance of 6, and the edge connecting
    #    it with a neighbor B has length 2, then the distance to B through A
    #    will be 6 + 2 = 8. If B was previously marked with a distance greater
    #    than 8 then change it to 8. Otherwise, the current value will be kept.

    # 4. When we are done considering all of the unvisited neighbors of the
    #    current node, mark the current node as visited and remove it from the
    #    unvisited set. A visited node will never be checked again (this is
    #    valid and optimal in connection with the behavior in step 6.: that the
    #    next nodes to visit will always be in the order of 'smallest distance
    #    from initial node first' so any visits after would have a greater
    #    distance).

    # 5. If the destination node has been marked visited (when planning a route
    #    between two specific nodes) or if the smallest tentative distance among
    #    the nodes in the unvisited set is infinity (when planning a complete
    #    traversal; occurs when there is no connection between the initial node
    #    and remaining unvisited nodes), then stop. The algorithm has finished.

    # 6. Otherwise, select the unvisited node that is marked with the smallest
    #    tentative distance, set it as the new current node, and go back to step 
    #    3.

class GameState:
    def __init__(self, resolutions):
        for resolution in resolutions:
            ice = SyntaxError("invalid arguments for GameState - must be a list of doubles of condition functions and GameStates")
            if type(resolution) != type(set()):
                raise ice
            if type(resolution[0]) != type(lambda: None):
                raise ice
            if type(resolution[1]) != GameState:
                raise ice

class Game:
    def __init__(self):
        pass