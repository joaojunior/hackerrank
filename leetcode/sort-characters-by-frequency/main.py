import heapq


class Solution:
    def frequency_sort(self, s: str) -> str:
        frequency = {}
        for c in s:
            frequency[c] = frequency.get(c, 0) + 1
        result = []
        items = []
        for c, qty in frequency.items():
            heapq.heappush(items, (qty, c))
        while items:
            item = heapq.heappop(items)
            result.insert(0, item[1]*item[0])
        return ''.join(result)
