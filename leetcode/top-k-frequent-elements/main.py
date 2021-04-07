import heapq
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) - 1
        items = [(value, key) for key, value in frequency.items()]
        heapq.heapify(items)
        result = []
        for i in range(k):
            result.append(heapq.heappop(items)[1])
        return result
