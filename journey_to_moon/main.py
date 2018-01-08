from collections import defaultdict


class Graph():
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self.edges = defaultdict(list)

    def add_edge(self, source, dest):
        self.edges[source].append(dest)
        self.edges[dest].append(source)

    def adjacents(self, node):
        return self.edges[node][:]

    def nodes(self):
        return list(range(self.number_of_nodes))


def count_nationality(graph):
    count = {}
    group = 0
    nodes = graph.nodes()
    visited = {}
    for node in nodes:
        visited[node] = False
    while nodes:
        node = nodes.pop(0)
        if visited[node] is False:
            queue = [node]
            while queue:
                node = queue.pop(0)
                if visited[node] is False:
                    visited[node] = True
                    count[group] = count.get(group, 0) + 1
                    for adjacent in graph.adjacents(node):
                        if visited[adjacent] is False:
                            queue.append(adjacent)
            group += 1
    return count


def journey_to_moon(graph):
    count = count_nationality(graph)
    number_nationality = len(count.keys())
    result = 0
    for i in range(number_nationality):
        for j in range(i + 1, number_nationality):
            result += count[i] * count[j]
    print(result)


if __name__ == '__main__':
    number_nodes, number_edges = input().split()
    number_nodes = int(number_nodes)
    number_edges = int(number_edges)
    graph = Graph(number_nodes)
    for i in range(number_edges):
        source, dest = input().split()
        source = int(source)
        dest = int(dest)
        graph.add_edge(source, dest)
    journey_to_moon(graph)
