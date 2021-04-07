from typing import List


class Interval:
    def __init__(self, s: int = 0, e: int = 0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals = sorted(intervals, key=lambda x: x.start)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i+1].start <= intervals[i].end:
                intervals[i+1].start = intervals[i].start
                intervals[i+1].end = max(intervals[i].end, intervals[i+1].end)
                intervals.pop(i)
            else:
                i += 1
        return intervals
