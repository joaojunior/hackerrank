from collections import defaultdict
import fractions


class Graph():
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self.edges = defaultdict(list)

    def nodes(self):
        return list(range(1, self.number_of_nodes + 1))

    def add_edge(self, source, dest):
        self.edges[source].append(dest)
        self.edges[dest].append(source)

    def adjacents(self, node):
        return self.edges[node][:]


def bfs(graph, root):
    visited = {}
    parent = {}
    nodes = graph.nodes()
    for node in nodes:
        visited[node] = False
        parent[node] = -1
    queue = [root]
    while queue:
        node = queue.pop(0)
        if visited[node] is False:
            visited[node] = True
            for adjacent in graph.adjacents(node):
                if visited[adjacent] is False:
                    parent[adjacent] = node
                    queue.append(adjacent)
    return parent


def story_tree(graph, parent_alice, k):
    win = 0
    nodes = graph.nodes()
    total_games = len(nodes)
    for root in nodes:
        parents = bfs(graph, root)
        quantity = 0
        for child, parent in parent_alice.items():
            if parents[child] == parent:
                quantity += 1
        if quantity >= k:
            win += 1
    if win == 0:
        total_games = 1
    else:
        gcd = fractions.gcd(win, total_games)
        win = int(win / gcd)
        total_games = int(total_games / gcd)
    print('{}/{}'.format(win, total_games))


if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        number_of_nodes = int(input())
        graph = Graph(number_of_nodes)
        for edge in range(number_of_nodes - 1):
            source, dest = input().split()
            source = int(source)
            dest = int(dest)
            graph.add_edge(source, dest)
        parent_alice = {}
        g, k = input().split()
        g = int(g)
        k = int(k)
        for j in range(g):
            parent, child = input().split()
            parent = int(parent)
            child = int(child)
            parent_alice[child] = parent
        story_tree(graph, parent_alice, k)
