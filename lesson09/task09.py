class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.step = 3
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return ((23 * sum + 53) % 79) % self.size

    def is_key(self, key):
        return self.seek_slot(key, key) is not None

    def put(self, key, value):
        slot = self.seek_slot(key, None)
        self.slots[slot] = key
        self.values[slot] = value

    def get(self, key):
        slot = self.seek_slot(key, key)
        if slot is None:
            return None
        return self.values[slot]

    def seek_slot(self, key, search_val):
        slot = self.hash_fun(key)
        i = 0
        while i < self.step:
            if self.slots[slot] == search_val or self.slots[slot] == key:
                return slot
            slot += self.step
            if slot >= self.size:
                slot -= self.size
                i += 1
        return None




