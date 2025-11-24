class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        val = self.peek()
        if val is None:
            return None
        del self.stack[-1]
        return val

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        val = self.stack[self.size() - 1]
        return val



