class Solution:
    def ladder_length(self, begin_word: str, end_word: str,
                      words: list) -> int:
        if end_word not in words:
            return 0

        self.size = len(begin_word)
        self.words = words
        self.end_word = end_word
        self.frequencies = {}
        for word in words + [begin_word]:
            frequency = {}
            for c in word:
                frequency[c] = frequency.get(c, 0) + 1
            self.frequencies[word] = frequency
        self.best = 0
        self.find(begin_word, 1, [begin_word])
        return self.best

    def find(self, begin_word: str, qty: int, words_used: list) -> int:
        if begin_word == self.end_word:
            if self.best == 0 or qty < self.best:
                self.best = qty
        else:
            for word in self.words:
                if word not in words_used:
                    if self.is_transformed(begin_word, word):
                        self.find(word, qty + 1, words_used[:] + [word])

    def is_transformed(self, word1: str, word2: str) -> bool:
        i = 0
        dif = 0
        while i < len(word1) and dif < 2:
            if word1[i] != word2[i]:
                dif += 1
            i += 1
        return dif < 2


if __name__ == '__main__':
    solution = Solution()
    begin_word = "leet"
    end_word = "code"
    words = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]

    print(solution.ladder_length(begin_word, end_word, words))
