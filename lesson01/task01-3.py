from unittest import TestCase

from ASD1.lesson01.task01 import Node, LinkedList


class TestLinkedList(TestCase):
    def setUp(self):
        self.list = LinkedList()
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(3))
        self.list.add_in_tail(Node(4))
        self.list.add_in_tail(Node(5))
        self.list.add_in_tail(Node(6))

    def test_len(self):
        list1 = LinkedList()
        self.assertEqual(list1.len(), 0)
        self.assertEqual(self.list.len(), 6)
        self.list.add_in_tail(Node(7))
        self.assertEqual(self.list.len(), 7)

    def test_find_all_empty(self):
        list1 = LinkedList()
        self.assertEqual(list1.find_all(55), [], 'should return None')

    def test_find_all_one_none(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(7))
        self.assertEqual(list1.find_all(55), [], 'should return None')

    def test_find_all_one_one(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(7))
        find_result = list1.find_all(7)
        self.assertEqual(len(find_result), 1)
        self.assertEqual(find_result[0].value, 7)

    def test_find_all_multy_one(self):
        self.list.add_in_tail(Node(7))
        find_result = self.list.find_all(1)
        self.assertEqual(len(find_result), 1)
        self.assertEqual(find_result[0].value, 1)

        find_result = self.list.find_all(4)
        self.assertEqual(len(find_result), 1)
        self.assertEqual(find_result[0].value, 4)

        find_result = self.list.find_all(6)
        self.assertEqual(len(find_result), 1)
        self.assertEqual(find_result[0].value, 6)

        find_result = self.list.find_all(7)
        self.assertEqual(len(find_result), 1)
        self.assertEqual(find_result[0].value, 7)

    def test_find_all_multy_many(self):
        self.list.add_in_tail(Node(1))
        find_result = self.list.find_all(1)
        self.assertEqual(len(find_result), 2)
        self.assertEqual(find_result[0].value, 1)
        self.assertEqual(find_result[1].value, 1)

        self.list.add_in_tail(Node(6))
        self.list.add_in_tail(Node(4))
        self.list.add_in_tail(Node(1))

        find_result = self.list.find_all(1)
        self.assertEqual(len(find_result), 3)
        self.assertEqual(find_result[0].value, 1)
        self.assertEqual(find_result[1].value, 1)
        self.assertEqual(find_result[2].value, 1)

        find_result = self.list.find_all(6)
        self.assertEqual(len(find_result), 2)
        self.assertEqual(find_result[0].value, 6)
        self.assertEqual(find_result[1].value, 6)

        find_result = self.list.find_all(4)
        self.assertEqual(len(find_result), 2)
        self.assertEqual(find_result[0].value, 4)
        self.assertEqual(find_result[1].value, 4)

    def test_find_all_multy_none(self):
        self.assertEqual(self.list.find_all(55), [], 'should return None')

    def test_delete_one_empty(self):
        list1 = LinkedList()
        list1.delete(55)
        self.assertIsNone(list1.head)
        self.assertIsNone(list1.tail)

    def test_delete_one_one_none(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(5))
        list1.delete(1)
        self.assertEqual(list1.head.value, 5)
        self.assertEqual(list1.tail.value, 5)
        self.assertIsNone(list1.head.next)
        self.assertIsNone(list1.tail.next)
        self.assertEqual(list1.len(), 1)

    def test_delete_one_one(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(5))
        list1.delete(5)
        self.assertIsNone(list1.head)
        self.assertIsNone(list1.tail)
        self.assertEqual(list1.len(), 0)

    def test_delete_one_many(self):
        self.list.delete(4)
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 1)
        self.assertEqual(self.list.tail.value, 6)
        self.assertEqual(self.list.head.next.next.next.value, 5)

    def test_delete_one_of_many_many(self):
        self.list.add_in_tail(Node(4))
        self.list.delete(4)
        self.assertEqual(self.list.len(), 6)
        self.assertEqual(self.list.head.value, 1)
        self.assertEqual(self.list.tail.value, 4)
        self.assertEqual(self.list.head.next.next.next.value, 5)
        find_result = self.list.find_all(4)
        self.assertEqual(len(find_result), 1)

    def test_delete_one_many_head(self):
        self.list.delete(1)
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.head.next.value, 3)


    def test_delete_one_many_tail(self):
        self.list.delete(6)
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 1)
        self.assertEqual(self.list.tail.value, 5)
        self.assertIsNone(self.list.tail.next)

    def test_delete_many_empty(self):
        self.list.delete(55, True)

    def test_delete_many_one(self):
        self.list.delete(4, True)
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 1)
        self.assertEqual(self.list.tail.value, 6)
        self.assertEqual(self.list.head.next.next.next.value, 5)

    def test_delete_many_one_head(self):
        self.list.delete(1, True)
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.head.next.value, 3)

    def test_delete_many_one_tail(self):
        self.list.delete(6, True)
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 1)
        self.assertEqual(self.list.tail.value, 5)
        self.assertIsNone(self.list.tail.next)

    def test_delete_many_many(self):
        self.list.add_in_tail(Node(4))
        self.list.add_in_tail(Node(5))
        self.list.add_in_tail(Node(4))
        self.list.add_in_tail(Node(2))
        self.assertEqual(self.list.len(), 10)
        self.list.delete(4, True)
        self.assertEqual(self.list.len(), 7)
        find_result = self.list.find_all(4)
        self.assertEqual(len(find_result), 0)

    def test_delete_many_many_head(self):
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(3))
        self.list.add_in_tail(Node(1))
        self.list.delete(1, True)
        self.assertEqual(self.list.len(), 6)
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.head.next.value, 3)
        self.assertEqual(self.list.tail.value, 3)

    def test_delete_many_many_tail(self):
        self.list.add_in_tail(Node(6))
        self.list.add_in_tail(Node(33))
        self.list.add_in_tail(Node(6))
        self.list.delete(6, True)
        self.assertEqual(self.list.len(), 6)
        self.assertEqual(self.list.tail.value, 33)

    def test_clean_empty(self):
        list1 = LinkedList()
        list1.clean()
        self.assertEqual(list1.len(), 0)
        self.assertIsNone(list1.head)
        self.assertIsNone(list1.tail)

    def test_clean_one(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(5))
        list1.clean()
        self.assertEqual(list1.len(), 0)
        self.assertIsNone(list1.head)
        self.assertIsNone(list1.tail)

    def test_clean_many(self):
        self.list.clean()
        self.assertEqual(self.list.len(), 0)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_insert_to_empty(self):
        list1 = LinkedList()
        list1.insert(None, Node(5))
        self.assertEqual(list1.len(), 1)
        self.assertEqual(list1.head.value, 5)
        self.assertEqual(list1.tail.value, 5)

    def test_insert_to_one(self):
        list1 = LinkedList()
        node1 = Node(5)
        list1.add_in_tail(node1)
        list1.insert(node1, Node(7))
        self.assertEqual(list1.len(), 2)
        self.assertEqual(list1.head.value, 5)
        self.assertEqual(list1.tail.value, 7)

    def test_insert_to_one_as_head(self):
        list1 = LinkedList()
        node1 = Node(5)
        list1.add_in_tail(node1)
        list1.insert(None, Node(7))
        self.assertEqual(list1.len(), 2)
        self.assertEqual(list1.head.value, 7)
        self.assertEqual(list1.tail.value, 5)

    def test_insert_to_many_to_mid(self):
        node = self.list.find(3)
        self.list.insert(node, Node(7))
        self.assertEqual(self.list.len(), 7)
        self.assertEqual(self.list.head.next.next.next.value, 7)
        self.assertEqual(self.list.head.next.next.next.value, 7)
        self.assertEqual(self.list.head.next.next.next.next.value, 4)

    def test_insert_to_many_as_head(self):
        self.list.insert(None, Node(7))
        self.assertEqual(self.list.len(), 7)
        self.assertEqual(self.list.head.value, 7)
        self.assertEqual(self.list.head.next.value, 1)

    def test_insert_to_many_as_tail(self):
        self.list.insert(self.list.tail, Node(7))
        self.assertEqual(self.list.len(), 7)
        self.assertEqual(self.list.tail.value, 7)