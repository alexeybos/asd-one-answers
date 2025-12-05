class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        new_node = Node(value)
        if self.__ascending:
            compare_result = -1
        else:
            compare_result = 1
        node = self.head
        if node is None:
            self.head = new_node
            self.tail = new_node
            return
        if self.compare(self.head.value, value) != compare_result:
            node.prev = new_node
            new_node.next = node
            self.head = new_node
            return
        if self.compare(self.tail.value, value) == compare_result:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        while node is not None and self.compare(node.value, value) == compare_result:
            node = node.next
        new_node.prev = node.prev
        new_node.prev.next = new_node
        node.prev = new_node
        new_node.next = node

    def find(self, val):
        node = self.head
        if self.__ascending:
            expected_compare_result = -1
        else:
            expected_compare_result = 1
        while node is not None:
            compare_result = self.compare(node.value, val)
            if compare_result == 0:
                return node
            if compare_result != expected_compare_result:
                return None
            node = node.next
        return None

    def delete(self, val):
        node = self.find(val)
        if node is None:
            return
        if node.prev is None and node.next is None:
            self.clean(self.__ascending)
            return
        if self.head == node:
            self.head = node.next
            node.next.prev = None
            return
        if self.tail == node:
            self.tail = node.prev
            node.prev.next = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev


    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):
        cnt = 0
        node = self.head
        while node is not None:
            cnt += 1
            node = node.next
        return cnt

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        str1 = v1.strip()
        str2 = v2.strip()
        if str1 == str2:
            return 0
        elif str1 > str2:
            return 1
        return -1



