from typing import List


class Solution:
    def h_index(self, citations: List[int]) -> int:
        citations = sorted(citations)
        result = 0
        size = len(citations)
        i = 0
        while i < size:
            h = size - i
            if len(citations[i:]) >= h:
                if i != 0:
                    if citations[i-1] <= h and citations[i] >= h:
                        return h
                else:
                    if citations[i] >= h:
                        return h
            i += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    citations = [3, 0, 6, 1, 5]
    print(solution.h_index(citations))
