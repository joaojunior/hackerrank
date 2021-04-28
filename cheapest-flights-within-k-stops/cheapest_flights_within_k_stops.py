from typing import Dict, List, Tuple


def bellman_ford(adjacents: Dict[int, List[Tuple[int]]], src: int,
                 dst: int, k: int) -> int:
    distances = {}
    for city in adjacents.keys():
        distances[(0, city)] = float('inf')
    distances[(0, src)] = 0
    for i in range(1, k+2):
        for city in adjacents.keys():
            distances[(i, city)] = distances[(i-1, city)]
        for _src, edges in adjacents.items():
            for _dst, distance in edges:
                distances[(i, _dst)] = min(distances[(i, _dst)],
                                           distances[(i-1, _src)] + distance)
    if distances[(k+1, dst)] < float('inf'):
        return distances[(k+1, dst)]
    return -1


class Solution:
    def find_cheapest_price(self, n: int, flights: List[List[int]],
                            src: int, dst: int, k: int) -> int:
        adjacents = {}
        for i in range(n):
            adjacents[i] = []
        for i, j, distance in flights:
            adjacents[i].append((j, distance))
        return bellman_ford(adjacents, src, dst, k)
