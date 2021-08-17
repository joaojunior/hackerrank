import math


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        total = m + n

        return math.factorial(total) // (math.factorial(m) * math.factorial(n))
