from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        result = 0
        while i < j:
            if height[i] < height[j]:
                area = (j - i) * height[i]
                i += 1
            else:
                area = (j - i) * height[j]
                j -= 1
            result = max(result, area)
        return result
