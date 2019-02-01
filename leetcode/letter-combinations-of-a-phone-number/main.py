class Solution:
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'),
                   '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
                   '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'),
                   '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        if digits == '':
            return []
        result = list(letters[digits[0]])
        for digit in digits[1:]:
            qty = 0
            size = len(result)
            while qty < size:
                new_combination = result.pop(0)
                for c in letters[digit]:
                    result.append(''.join([new_combination[:], c]))
                qty += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    digits = '22'
    print(solution.letter_combinations(digits))
