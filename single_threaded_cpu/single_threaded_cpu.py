import heapq
from typing import List


class Solution:
    def get_order(self, tasks: List[List[int]]) -> List[int]:
        time = 1
        q = []
        q_tasks = []
        result = []
        for i in range(len(tasks)):
            q_tasks.append((tasks[i][0], tasks[i][1], i))
        heapq.heapify(q_tasks)
        while q_tasks or q:
            while q_tasks and q_tasks[0][0] <= time:
                enqueue_time, processing_time, i = heapq.heappop(q_tasks)
                heapq.heappush(q, (processing_time, i))
            if q:
                processing_time, i = heapq.heappop(q)
                time += processing_time
                result.append(i)
            else:
                time = q_tasks[0][0]
        return result
