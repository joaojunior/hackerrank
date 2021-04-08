from typing import List


class Solution:
    def find_min_arrow_shots(self, points: List[List[int]]) -> int:
        arrows = 0
        if points:
            arrows = 1
            points.sort(key=lambda x: (x[0], x[1]))
            last = points[0]
            for point in points[1:]:
                if point[0] <= last[1]:
                    last[0] = max(last[0], point[1])
                    last[1] = min(last[1], point[1])
                else:
                    arrows += 1
                    last = point
        return arrows
