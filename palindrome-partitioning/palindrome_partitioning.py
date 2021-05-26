from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.partitions = []
        self.generate_partitions(s, [])
        return self.partitions

    def generate_partitions(self, s, partition, start=0, end=1):
        if end == len(s):
            if self.is_palindrome(s[start:end]):
                partition.append(s[start:end])
                self.partitions.append(partition)
        else:
            if self.is_palindrome(s[start:end]):
                self.generate_partitions(s, partition[:] + [s[start:end]],
                                         end, end + 1)
            self.generate_partitions(s, partition[:], start, end + 1)

    def is_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
