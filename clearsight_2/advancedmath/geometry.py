class MetricSpace:
    def __init__(self, nodes, metric):
        self.nodes = nodes
        self.metric = metric

    def distance(self, node1, node2):
        return self.metric(node1, node2)