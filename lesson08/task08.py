class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return ((23 * sum + 53) % 79) % 17

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        i = 0
        while i < self.step:
            if self.slots[slot] is None:
                return slot
            slot += self.step
            if slot >= self.size:
                slot -= self.size
                i += 1
        return None

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value):
        slot = self.hash_fun(value)
        i = 0
        if slot is None:
            return None
        while i < self.step:
            if self.slots[slot] == value:
                return slot
            slot += self.step
            if slot >= self.size:
                slot -= self.size
                i += 1
        return None




