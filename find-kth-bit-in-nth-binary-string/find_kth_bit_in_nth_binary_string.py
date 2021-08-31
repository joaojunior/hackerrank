class Solution:
    def find_kth_bit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(n-1):
            s = self.generate_string(s)
        return s[k-1]

    def generate_string(self, s: str) -> str:
        return ''.join([s, '1', self.reverse(self.invert(s))])

    def reverse(self, s: str) -> str:
        new_s = []
        i = len(s) - 1
        while i >= 0:
            new_s.append(s[i])
            i -= 1
        return ''.join(new_s)

    def invert(self, s: str) -> str:
        new_s = []
        for c in s:
            if c == '0':
                new_s.append('1')
            else:
                new_s.append('0')
        return ''.join(new_s)
