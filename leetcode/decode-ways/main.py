class Solution:
    def num_decodings(self, s: str) -> int:
        self.memoize = {}
        return self.find(s)

    def find(self, s):
        if s in self.memoize:
            return self.memoize[s]
        elif s == '':
            return 1
        else:
            qty = 0
            if int(s[:1]) > 0:
                qty = self.find(s[1:])
                self.memoize[s[1:]] = qty
            if len(s) >= 2 and 0 < int(s[:2]) <= 26 and s[0] != '0':
                qty += self.find(s[2:])
                self.memoize[s[2:]] = qty - self.memoize[s[1:]]
            return qty


if __name__ == '__main__':
    solution = Solution()
    s = ('927297167251227735495393942768951823971422829346'
         '3398742522722274929422229859968434281231132695842184')
    print(solution.num_decodings(s))
