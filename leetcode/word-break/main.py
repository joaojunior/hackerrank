from typing import List


class Solution():
    def word_break(self, s: str, words: List[str]) -> bool:
        self.words = words
        self.memoization = {}
        return self.find(s)

    def find(self, s: str) -> bool:
        if s in self.memoization:
            return self.memoization[s]
        if s == '':
            return True
        else:
            result = False
            i = 0
            while i < len(self.words) and result is False:
                word = self.words[i]
                if s.startswith(word):
                    result = self.find(s[len(word):])
                    self.memoization[s[len(word):]] = result
                i += 1
            return result


if __name__ == '__main__':
    solution = Solution()
    s = "catsandog"
    words = ["cats", "dog", "sand", "and", "cat"]
    print(solution.word_break(s, words))
