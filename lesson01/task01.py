class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        while node != None:
            if node.value == val:
                find_result.append(node)
            node = node.next
        return find_result

    def delete(self, val, all=False):
        node = self.head
        prev_node = None
        while node is not None:
            if node.value == val:
                if self.head == node:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                if self.tail == node:
                    self.tail = prev_node
                if not all:
                    return
            else:
                prev_node = node
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
            newNode.next = self.head
            self.head = newNode
            if newNode.next is None:
                self.tail = newNode
            return

        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                if node == self.tail:
                    self.tail = newNode
            node = node.next



