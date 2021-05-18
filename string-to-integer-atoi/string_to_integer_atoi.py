class Solution:
    def my_atoi(self, s: str) -> int:
        result = 0
        power = 1
        digits = []
        signal = 1
        i = 0
        n = len(s)
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '-':
                signal = -1
                i += 1
                break
            elif s[i] == '+':
                signal = 1
                i += 1
                break
            else:
                break
        while i < n:
            c = s[i]
            if c.isdigit():
                digits.append(int(c))
            else:
                break
            i += 1
        power = 1
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            result += digit * power
            power *= 10
        result *= signal
        min_ = - 2 ** 31
        max_ = 2 ** 31 - 1
        if result < min_:
            result = min_
        if result > max_:
            result = max_
        return result
