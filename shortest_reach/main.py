from collections import defaultdict


class Graph():
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self.edges = defaultdict(list)

    def nodes(self):
        return list(range(1, self.number_of_nodes + 1))

    def adjacents(self, node):
        return self.edges[node][:]

    def add_edge(self, source, dest):
        self.edges[source].append(dest)
        self.edges[dest].append(source)


def bfs(graph, source):
    visited = {}
    levels = {}
    for node in graph.nodes():
        visited[node] = False
        levels[node] = -1
    queue = [(source, 0)]
    while queue:
        node, level = queue.pop(0)
        if visited[node] is False:
            visited[node] = True
            level += 1
            for adjacent in graph.adjacents(node):
                if visited[adjacent] is False and levels[adjacent] == -1:
                    queue.append((adjacent, level))
                    levels[adjacent] = level
    return levels


def shortest_reach(graph, source, size=6):
    levels = bfs(graph, source)
    for node in graph.nodes():
        if node != source:
            level = levels[node]
            if level != -1:
                level *= size
            print(level, end=' ')


if __name__ == '__main__':
    q = input()
    q = int(q)
    for i in range(q):
        number_of_nodes, number_of_edges = input().split()
        number_of_nodes = int(number_of_nodes)
        number_of_edges = int(number_of_edges)
        graph = Graph(number_of_nodes)
        for edge in range(number_of_edges):
            source, dest = input().split()
            source = int(source)
            dest = int(dest)
            graph.add_edge(source, dest)
        source = input()
        source = int(source)
        shortest_reach(graph, source)
        print()
