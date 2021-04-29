import heapq


class Solution:
    def maximum_score(self, a: int, b: int, c: int) -> int:
        qty = 0
        q = [-a, -b, -c]
        heapq.heapify(q)
        while len(q) > 1:
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            qty += 1
            if a + 1 < 0:
                heapq.heappush(q, a + 1)
            if b + 1 < 0:
                heapq.heappush(q, b + 1)
        return qty
