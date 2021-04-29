from typing import List, Tuple


class IndexMinHeap:
    def __init__(self):
        self.items = []
        self.indexes = {}

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def insert(self, key: int, value: int):
        i = self.indexes.get(key, None)
        if i is not None:
            _, old_value = self.items[i]
            self.items[i] = (key, value + old_value)
            self.heapify_down(i)
        else:
            i = len(self.items)
            self.items.append((key, value))
            self.indexes[key] = i
            self.heapify(i)

    def delete_min(self) -> Tuple[int]:
        key, value = self.items[0]
        self.indexes.pop(key)
        if len(self.items) > 1:
            self.items[0] = self.items[-1]
            self.indexes[self.items[0][0]] = 0
        self.items.pop()
        self.heapify_down(0)
        return (key, value)

    def heapify_down(self, i: int):
        left = 2 * i + 1
        right = left + 1
        size = len(self.items)
        if left < size:
            j = i
            if self.items[j][0] > self.items[left][0]:
                j = left
            if right < size and self.items[j][0] > self.items[right][0]:
                j = right
            if i != j:
                self.items[i], self.items[j] = self.items[j], self.items[i]
                self.indexes[self.items[i][0]] = i
                self.indexes[self.items[j][0]] = j
                self.heapify_down(j)

    def heapify(self, i: int):
        if i > 0:
            parent = (i - 1) // 2
            if self.items[i][0] < self.items[parent][0]:
                self.items[i], self.items[parent] = (self.items[parent],
                                                     self.items[i])
                self.indexes[self.items[i][0]] = i
                self.indexes[self.items[parent][0]] = parent
                self.heapify(parent)


class Solution:
    def eaten_apples(self, apples: List[int], days: List[int]) -> int:
        qty = 0
        i = 0
        size = len(apples)
        index_min_heap = IndexMinHeap()
        while i < size or not index_min_heap.is_empty():
            if i < size:
                apple = apples[i]
                day = days[i]
                if apple > 0:
                    index_min_heap.insert(i + day, apple)
            deadline = 0
            while deadline <= i and not index_min_heap.is_empty():
                deadline, apple = index_min_heap.delete_min()
                if deadline > i:
                    qty += 1
                    if apple - 1 > 0:
                        index_min_heap.insert(deadline, apple - 1)
            i += 1
        return qty
