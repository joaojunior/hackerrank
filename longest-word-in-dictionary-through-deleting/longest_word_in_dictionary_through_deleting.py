from typing import List


class Solution:
    def find_longest_word(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(word):
                return word
        return ''
