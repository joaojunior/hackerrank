from typing import Dict, List


class MinHeap():
    def __init__(self):
        self.items = []
        self.lt = {}

    def heapify_up(self, i: int):
        if i > 0:
            parent = (i - 1) // 2
            if self.items[parent][1] > self.items[i][1]:
                self.items[parent], self.items[i] = (self.items[i],
                                                     self.items[parent])
                self.lt[self.items[parent][0]] = parent
                self.lt[self.items[i][0]] = i
                self.heapify_up(parent)

    def update_key(self, key: int, value: int):
        if key in self.lt:
            i = self.lt[key]
            self.items[i] = [key, value]
            self.heapify_up(i)
        else:
            self.items.append([key, value])
            size = len(self.items)
            self.lt[key] = size - 1
            self.heapify_up(size - 1)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def extract_min(self) -> int:
        key = self.items[0][0]
        self.lt.pop(key)
        self.items[0] = self.items[-1]
        self.lt[self.items[0][0]] = 0
        self.items.pop()
        self.heapify(0)
        return key

    def heapify(self, i: int):
        left = i * 2 + 1
        right = left + 1
        if left < len(self.items):
            j = i
            if self.items[j][1] > self.items[left][1]:
                j = left
            if right < len(self.items) and (self.items[j][1] >
                                            self.items[right][1]):
                j = right
            if i != j:
                self.items[i], self.items[j] = self.items[j], self.items[i]
                self.lt[self.items[i][0]] = i
                self.lt[self.items[j][0]] = j
                self.heapify(j)


def dijkstra(adjacents: Dict[int, List], s: int, n: int) -> Dict[int, int]:
    distances = {}
    visited = {}
    inf = float("Inf")
    for key in range(1, n+1):
        visited[key] = 0
        distances[key] = inf
    distances[s] = 0
    min_heap = MinHeap()
    min_heap.update_key(s, 0)
    while not min_heap.is_empty():
        i = min_heap.extract_min()
        visited[i] = 1
        for j, cost in adjacents[i]:
            if visited[j] == 0:
                if distances[i] + cost < distances[j]:
                    distances[j] = distances[i] + cost
                    min_heap.update_key(j, distances[j])
    return distances


class Solution:
    def network_delay_time(self, times: List[List[int]],
                           n: int, k: int) -> int:
        adjacents = {}
        for i in range(n + 1):
            adjacents[i] = []
        for s, d, cost in times:
            edges = adjacents.get(s, [])
            edges.append((d, cost))
            adjacents[s] = edges
        distances = dijkstra(adjacents, k, n)
        result = max(distances.values())
        if result == float("inf"):
            result = -1
        return result
