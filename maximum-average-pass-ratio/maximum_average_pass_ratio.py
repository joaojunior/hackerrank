import heapq
from typing import List


class Solution:
    def max_average_ratio(self, classes: List[List[int]],
                          extra_students: int) -> float:
        q = []
        for passes, total in classes:
            q.append((-((passes+1)/(total+1)-passes/total), passes, total))
        heapq.heapify(q)
        for i in range(extra_students):
            _, passes, total = heapq.heappop(q)
            passes += 1
            total += 1
            heapq.heappush(
                q, (-((passes+1)/(total+1)-passes/total), passes, total))
        result = 0
        for _, passes, total in q:
            result += passes/total
        return result / len(q)
