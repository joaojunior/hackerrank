class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        new = None
        map_ = {}
        if node is not None:
            queue = [node]
            while queue:
                node = queue.pop(0)
                if new is None:
                    new = UndirectedGraphNode(node.label)
                    root = new
                else:
                    if id(node) not in map_:
                        root = UndirectedGraphNode(node.label)
                    else:
                        root = map_[id(node)]
                for n in node.neighbors:
                    if id(n) not in map_:
                        n1 = UndirectedGraphNode(n.label)
                        root.neighbors.append(n1)
                        queue.append(n)
                        map_[id(n)] = n1
                    else:
                        root.neighbors.append(map_[id(n)])
        return new
