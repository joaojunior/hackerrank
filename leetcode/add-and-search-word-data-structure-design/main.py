class WordDictionary:
    def __init__(self):
        self.letters = {}
        self.is_end = False

    def add_word(self, word: str):
        trie = self
        for c in word:
            if c in trie.letters:
                trie = trie.letters[c]
            else:
                trie.letters[c] = WordDictionary()
                trie = trie.letters[c]
        trie.is_end = True

    def search(self, word: str, trie=None) -> bool:
        if trie is None:
            trie = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for t in trie.letters.values():
                    result = self.search(word[i+1:], t)
                    if result is True:
                        return True
                return False
            else:
                if c in trie.letters:
                    trie = trie.letters[c]
                else:
                    return False
        return trie.is_end
