class Solution:
    def num_decodings(self, s: str) -> int:
        return self.find(s)

    def find(self, s):
        if s == '':
            return 1
        else:
            qty = 0
            if int(s[:1]) > 0:
                qty = self.find(s[1:])
            if len(s) >= 2 and 0 < int(s[:2]) <= 26 and s[0] != '0':
                qty += self.find(s[2:])
            return qty


if __name__ == '__main__':
    solution = Solution()
    s = '01'
    print(solution.num_decodings(s))
