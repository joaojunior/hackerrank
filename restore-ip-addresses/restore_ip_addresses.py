from typing import List


class Solution:
    def restore_ip_addresses(self, s: str) -> List[str]:
        if s == "":
            return []
        self.s = s
        self.size = len(s)
        self.result = []
        self.partitions(0, 1, [])
        return self.result

    def partitions(self, start: int = 0, end: int = 1, partition: List = None):
        if end == self.size:
            if self.is_valid(self.s[start:end]):
                partition.append(self.s[start:end])
                if len(partition) == 4:
                    self.result.append('.'.join(partition))
        else:
            self.partitions(start, end+1, partition[:])
            if (len(partition) + 1 <= 4) and self.is_valid(self.s[start:end]):
                self.partitions(end, end+1, partition[:] + [self.s[start:end]])

    def is_valid(self, s: str) -> bool:
        i = 0
        while i < len(s) and s[i] == '0':
            i += 1
        if i > 0 and len(s) > 1:
            return False
        return len(s) <= 3 and int(s) <= 255
