from collections import defaultdict


class Graph():
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self._edges = {}
        self._adjacents = defaultdict(list)

    def nodes(self):
        return list(range(1, self.number_of_nodes + 1))

    def edges(self):
        return self._edges.keys()

    def add_edge(self, source, dest):
        self._edges[(source, dest)] = True
        self._adjacents[source].append(dest)
        self._adjacents[dest].append(source)

    def remove_edge(self, edge):
        self._edges[edge] = False

    def return_edge(self, edge):
        self._edges[edge] = True

    def adjacents(self, node):
        result = []
        for dest in self._adjacents[node]:
            edge_exist = self._edges.get((node, dest), False)
            if edge_exist or self._edges.get((dest, node), False):
                result.append(dest)
        return result

    def edge_not_connected_leaf(self, edge):
        adjacents = self.adjacents(edge[0])
        if len(adjacents) > 1:
            adjacents = self.adjacents(edge[1])
            if len(adjacents) > 1:
                return True
        return False


def bfs(graph, node):
    visited = {}
    queue = [node]
    for node in graph.nodes():
        visited[node] = False
    while queue:
        node = queue.pop(0)
        if visited[node] is False:
            visited[node] = True
            for adjacent in graph.adjacents(node):
                if visited[adjacent] is False:
                    queue.append(adjacent)
    component = []
    for key, value in visited.items():
        if value is True:
            component.append(key)
    return component


def even_tree(graph):
    number_removed_edges = 0
    for edge in graph.edges():
        if graph.edge_not_connected_leaf(edge):
            graph.remove_edge(edge)
            removed = True
            nodes = graph.nodes()
            while nodes and removed:
                node = nodes.pop(0)
                component = bfs(graph, node)
                if len(component) % 2 == 0:
                    for node in component:
                        if node in nodes:
                            nodes.remove(node)
                else:
                    removed = False
            if removed is True:
                number_removed_edges += 1
            else:
                graph.return_edge(edge)
    return number_removed_edges


if __name__ == '__main__':
    number_of_nodes, number_of_edges = input().split()
    number_of_nodes = int(number_of_nodes)
    number_of_edges = int(number_of_edges)
    graph = Graph(number_of_nodes)
    for edge in range(number_of_edges):
        source, dest = input().split()
        graph.add_edge(int(source), int(dest))
    print(even_tree(graph))
