class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        self.result = 0
        self.s = s
        self.memoization = {}
        self.verify(0, len(s) - 1)
        return self.result

    def verify(self, start: int, end: int):
        repeated = False
        if end >= start:
            j = start
            frequency = {}
            while j <= end and repeated is False:
                c = self.s[j]
                if c not in frequency:
                    frequency[c] = 1
                else:
                    repeated = True
                j += 1
            self.memoization[self.s[start:end+1]] = end - start + 1
            if repeated is False:
                if end - start + 1 > self.result:
                    self.result = end - start + 1
            else:
                if end - start > self.result:
                    if self.s[start+1:end+1] not in self.memoization:
                        self.verify(start+1, end)
                    if self.s[start:end] not in self.memoization:
                        self.verify(start, end-1)


if __name__ == '__main__':
    solution = Solution()
    s = 'lmaygfgihqznazgdmzqcpiuudjucv'
    print(solution.length_of_longest_substring(s))
