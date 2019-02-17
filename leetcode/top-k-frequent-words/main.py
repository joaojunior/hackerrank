from typing import List
import heapq


class Solution:
    def top_k_frequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) - 1
        result = []
        items = [(item[1], item[0]) for item in frequency.items()]
        heapq.heapify(items)
        for i in range(k):
            result.append(heapq.heappop(items)[1])
        return result
