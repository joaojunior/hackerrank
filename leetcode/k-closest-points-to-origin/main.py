from typing import List
import math
import heapq


class Solution:
    def k_closest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = []
        for point in points:
            distance = self.distance(point)
            if len(result) < K:
                heapq.heappush(result, (-distance, point))
            else:
                heapq.heappushpop(result, (-distance, point))
        return [item[1] for item in result]

    def distance(self, point1, point2=(0, 0)):
        return math.sqrt((point1[0] - point2[0])**2 +
                         (point1[1] - point2[1])**2)
