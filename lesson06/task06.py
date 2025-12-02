class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.append(item)

    def addTail(self, item):
        self.deque.insert(0, item)

    def removeFront(self):
        if self.size() == 0:
            return None
        return self.deque.pop()

    def removeTail(self):
        if self.size() == 0:
            return None
        return self.deque.pop(0)

    def size(self):
        return len(self.deque)





