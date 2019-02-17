from typing import List


class Trie:
    def __init__(self):
        self.letters = {}
        self.is_end = False


class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def build_dict(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            trie = self.trie
            for c in word:
                if c in trie.letters:
                    trie = trie.letters[c]
                else:
                    trie.letters[c] = Trie()
                    trie = trie.letters[c]
            trie.is_end = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for i in range(len(word)):
            c = word[i]
            if c in trie.letters:
                for c1, _trie in trie.letters.items():
                    if c != c1:
                        result = self._search(word[i+1:], _trie)
                        if result is True:
                            return True
                trie = trie.letters[c]
            else:
                for _trie in trie.letters.values():
                    result = self._search(word[i+1:], _trie)
                    if result is True:
                        return True
                return False
        return False

    def _search(self, word: str, trie: Trie) -> bool:
        for c in word:
            if c in trie.letters:
                trie = trie.letters[c]
            else:
                return False
        return trie.is_end
