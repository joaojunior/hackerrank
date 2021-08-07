from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        distances = {}
        visited = {}
        for i in range(size):
            distances[i] = size
            visited[i] = False
        distances[0] = 0
        q = [0]
        while q:
            i = q.pop(0)
            visited[i] = True
            for j in range(i+1, min(i + nums[i] + 1, size)):
                if distances[i] + 1 < distances[j]:
                    distances[j] = distances[i] + 1
                    if visited[j] is False:
                        q.append(j)
        return distances[size - 1]
