from typing import Dict


class Solution:
    def min_window(self, s: str, t: str) -> str:
        frequency_s = {}
        frequency_t = {}
        for c in s:
            frequency_s[c] = frequency_s.get(c, 0) + 1
        for c in t:
            frequency_t[c] = frequency_t.get(c, 0) + 1
        start = 0
        end = len(s) - 1
        result = ''
        while end >= start and start >= 0:
            if self.verify(frequency_s, frequency_t):
                result = s[start:end+1]
                frequency_s[s[start]] -= 1
                start += 1
            else:
                frequency_s[s[start-1]] += 1
                frequency_s[s[end]] -= 1
                start -= 1
                end -= 1
        return result

    def verify(self, frequency: Dict, frequency_t: Dict) -> bool:
        for c, qty in frequency_t.items():
            if frequency.get(c, 0) < qty:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.min_window(s, t))
