class HashTable:
    def __init__(self, capacity=101):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def _probe(self, key):
        index = hash(key) % self.capacity
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity
        return index

    def insert(self, key, value):
        index = self._probe(key)
        if self.table[index] is None:
            self.size += 1
        self.table[index] = (key, value)

    def get(self, key):
        index = self._probe(key)
        if self.table[index] is None:
            return None
        return self.table[index][1]

    def delete(self, key):
        index = self._probe(key)
        if self.table[index] is not None:
            self.table[index] = None
            self.size -= 1