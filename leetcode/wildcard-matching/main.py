class Solution:
    def is_match(self, s: str, p: str, memoization: dict = {}) -> bool:
        if (s, p) in memoization:
            return memoization[(s, p)]
        elif len(s) == 0:
            for c in p:
                if c != '*':
                    return False
            return True
        elif len(p) > 0:
            if s[0] == p[0] or p[0] == '?':
                memoization[s[1:], p[1:]] = self.is_match(s[1:], p[1:])
                return memoization[s[1:], p[1:]]
            elif p[0] == '*':
                result = self.is_match(s[0:], p[1:])
                if result is True:
                    return result
                else:
                    memoization[s[1:], p[0:]] = self.is_match(s[1:], p[0:])
                    return memoization[s[1:], p[0:]]
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    s = "zacabz"
    p = "*a?b*"
    print(solution.is_match(s, p))
