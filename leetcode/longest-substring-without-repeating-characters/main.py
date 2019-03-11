class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        result = 0
        size = len(s)
        for start in range(size):
            i = start
            frequency = {}
            repeated = False
            while repeated is False and i < size:
                c = s[i]
                if c not in frequency:
                    frequency[c] = 1
                    i += 1
                else:
                    repeated = True
            if i - start > result:
                result = i - start
        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'lmaygfgihqznazgdmzqcpiuudjucv'
    print(solution.length_of_longest_substring(s))
