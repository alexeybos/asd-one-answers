class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        find_result = []
        node = self.head
        while node is not None:
            if node.value == val:
                find_result.append(node)
            node = node.next
        return find_result

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if self.head == node:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                if self.tail == node:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        cnt = 0
        while node != None:
            cnt += 1
            node = node.next
        return cnt

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode is None:
            self.add_in_tail(newNode)
            return
        while node is not None:
            if node == afterNode:
                newNode.prev = node
                newNode.next = node.next
                node.next = newNode
                if self.tail == node:
                    self.tail = newNode
                else:
                    newNode.next.prev = newNode
            node = node.next

    def add_in_head(self, newNode):
        newNode.next = self.head
        newNode.prev = None
        if self.head == None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode



