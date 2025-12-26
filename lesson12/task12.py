class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.step = 3

    def hash_fun(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return ((23 * sum + 53) % 79) % self.size

    def is_key(self, key):
        return self.seek_slot(key, key) is not None

    def put(self, key, value):
        slot = self.seek_slot(key, None)
        if slot is not None:
            self.slots[slot] = key
            self.values[slot] = value
            self.hits[slot] += 1
            return
        min_hits = self.hits[0]
        remove_slot = 0
        for i in range(1, self.size):
            if self.hits[i] < min_hits:
                min_hits = self.hits[i]
                remove_slot = i
        self.slots[remove_slot] = key
        self.values[remove_slot] = value
        self.hits[remove_slot] = 0

    def get(self, key):
        slot = self.seek_slot(key, key)
        if slot is None:
            return None
        self.hits[slot] += 1
        return self.values[slot]

    def seek_slot(self, key, search_val):
        slot = self.hash_fun(key)
        i = 0
        while i <= self.step:
            while slot < self.size:
                if self.slots[slot] == search_val or self.slots[slot] == key:
                    return slot
                slot += self.step
            slot -= self.size
            i += 1
        return None




