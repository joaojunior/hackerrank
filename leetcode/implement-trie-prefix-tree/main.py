class Trie(object):
    def __init__(self):
        self.links = {}
        self.is_end = False

    def insert(self, word: str):
        trie = self
        for c in word:
            if c in trie.links:
                trie = trie.links[c]
            else:
                trie.links[c] = Trie()
                trie = trie.links[c]
        trie.is_end = True

    def search(self, word: str) -> bool:
        trie = self
        for c in word:
            if c in trie.links:
                trie = trie.links[c]
            else:
                return False
        return trie.is_end

    def starts_with(self, prefix: str) -> bool:
        links = self.links
        for c in prefix:
            if c in links:
                links = links[c].links
            else:
                return False
        return True
