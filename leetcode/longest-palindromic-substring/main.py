class Solution:
    def longest_palindrome(self, s: str) -> str:
        result = ''
        size = len(s)
        for start in range(size):
            i = size - 1
            while self.is_palindrome(s[start:i+1]) is False and i >= start:
                i -= 1
            if i >= start and i - start + 1 > len(result):
                result = s[start:i+1]
        return result

    def is_palindrome(self, s):
        start = 0
        end = len(s) - 1
        while end >= start:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
