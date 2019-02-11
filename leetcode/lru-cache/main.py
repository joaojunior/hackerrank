class LRUCache:
    def __init__(self, capacity: 'int'):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self._update_lru(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self._update_lru(key)
            self.cache[key] = value
        elif self.size + 1 <= self.capacity:
            self.size += 1
            self.cache[key] = value
            self.lru.insert(0, key)
        else:
            self.cache.pop(self.lru.pop())
            self.size -= 1
            self.put(key, value)

    def _update_lru(self, key: int):
        self.lru.remove(key)
        self.lru.insert(0, key)
