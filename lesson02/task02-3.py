from unittest import TestCase

from ASD1.lesson02.task02 import Node, LinkedList2

class TestLinkedList2(TestCase):
    def setUp(self):
        self.list = LinkedList2()
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(3))
        self.list.add_in_tail(Node(4))

    def test_len(self):
        list1 = LinkedList2()
        self.assertEqual(list1.len(), 0)
        list1.add_in_tail(Node(1))
        self.assertEqual(list1.len(), 1)
        self.assertEqual(self.list.len(), 4)

    def test_find_empty(self):
        list1 = LinkedList2()
        self.assertIsNone(list1.find(2))

    def test_find_in_one_yes(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(1))
        find_result = list1.find(1)
        self.assertEqual(find_result.value, 1)

    def test_find_in_one_no(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(1))
        find_result = list1.find(5)
        self.assertIsNone(find_result)

    def test_find_in_many_yes(self):
        find_result = self.list.find(4)
        self.assertEqual(find_result.value, 4)

    def test_find_in_many_first_of_many(self):
        self.list.add_in_tail(Node(1))
        find_result = self.list.find(1)
        self.assertEqual(find_result.value, 1)
        self.assertEqual(find_result.next.value, 2)

    def test_find_in_many_no(self):
        find_result = self.list.find(5)
        self.assertIsNone(find_result)

    def test_find_all_empty(self):
        list1 = LinkedList2()
        self.assertEqual(len(list1.find_all(2)), 0)

    def test_find_all_in_one_yes(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(1))
        find_result = list1.find_all(1)
        self.assertEqual(len(find_result), 1)
        self.assertEqual(find_result[0].value, 1)

    def test_find_all_in_one_no(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(1))
        find_result = list1.find_all(5)
        self.assertEqual(len(find_result), 0)

    def test_find_all_in_many_one(self):
        find_result = self.list.find_all(3)
        self.assertEqual(len(find_result), 1)

    def test_find_all_in_many_one_head(self):
        find_result = self.list.find_all(1)
        self.assertEqual(len(find_result), 1)
        self.assertEqual(find_result[0].value, 1)

    def test_find_all_in_many_one_tail(self):
        find_result = self.list.find_all(4)
        self.assertEqual(len(find_result), 1)
        self.assertEqual(find_result[0].value, 4)

    def test_find_all_in_many_many(self):
        self.list.add_in_tail(Node(1))
        find_result = self.list.find_all(1)
        self.assertEqual(len(find_result), 2)
        self.assertEqual(find_result[0].value, 1)
        self.assertEqual(find_result[1].value, 1)

    def test_find_all_in_many_no(self):
        find_result = self.list.find_all(5)
        self.assertEqual(len(find_result), 0)

    def test_delete_one_empty(self):
        list1 = LinkedList2()
        list1.delete(55)
        self.assertEqual(list1.len(), 0)

    def test_delete_one_in_one_yes(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(3))
        self.assertEqual(list1.len(), 1)
        list1.delete(3)
        self.assertEqual(list1.len(), 0)

    def test_delete_one_in_one_no(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(1))
        list1.delete(55)
        self.assertEqual(list1.len(), 1)

    def test_delete_one_in_many_one(self):
        self.assertEqual(self.list.len(), 4)
        self.list.delete(3)
        self.assertEqual(self.list.len(), 3)

    def test_delete_one_in_many_many(self):
        self.list.add_in_tail(Node(3))
        self.assertEqual(self.list.len(), 5)
        self.list.delete(3)
        self.assertEqual(self.list.len(), 4)

    def test_delete_one_in_many_no(self):
        self.list.delete(55)
        self.assertEqual(self.list.len(), 4)

    def test_delete_one_in_many_many_with_head(self):
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(3))
        self.list.add_in_tail(Node(4))
        self.assertEqual(self.list.len(), 7)
        self.list.delete(1)
        self.assertEqual(self.list.len(), 6)
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.head.next.value, 3)

    def test_delete_one_in_many_many_with_tail(self):
        self.assertEqual(self.list.len(), 4)
        self.assertEqual(self.list.tail.value, 4)
        self.list.delete(4)
        self.assertEqual(self.list.len(), 3)
        self.assertEqual(self.list.tail.value, 3)

    def test_delete_one_in_many_many_with_head_tail(self):
        self.list.add_in_tail(Node(1))
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.tail.value, 1)
        self.list.delete(1)
        self.assertEqual(self.list.len(), 4)
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.tail.value, 1)

    def test_delete_all_empty(self):
        list1 = LinkedList2()
        list1.delete(55, True)
        self.assertEqual(list1.len(), 0)

    def test_delete_all_in_one_yes(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(3))
        self.assertEqual(list1.len(), 1)
        list1.delete(3, True)
        self.assertEqual(list1.len(), 0)

    def test_delete_all_in_one_no(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(1))
        list1.delete(55, True)
        self.assertEqual(list1.len(), 1)

    def test_delete_all_in_many_one(self):
        self.assertEqual(self.list.len(), 4)
        self.list.delete(3, True)
        self.assertEqual(self.list.len(), 3)

    def test_delete_all_in_many_many(self):
        self.list.add_in_tail(Node(3))
        self.assertEqual(self.list.len(), 5)
        self.list.delete(3, True)
        self.assertEqual(self.list.len(), 3)

    def test_delete_all_in_many_no(self):
        self.list.delete(55, True)
        self.assertEqual(self.list.len(), 4)

    def test_delete_all_in_many_many_with_head(self):
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(3))
        self.list.add_in_tail(Node(4))
        self.assertEqual(self.list.len(), 7)
        self.list.delete(1, True)
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.head.next.value, 3)

    def test_delete_all_in_many_many_with_tail(self):
        self.list.add_in_tail(Node(3))
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.tail.value, 3)
        self.list.delete(3, True)
        self.assertEqual(self.list.len(), 3)
        self.assertEqual(self.list.tail.value, 4)

    def test_delete_all_in_many_many_with_head_tail(self):
        self.list.add_in_tail(Node(1))
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.tail.value, 1)
        self.list.delete(1, True)
        self.assertEqual(self.list.len(), 3)
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.tail.value, 4)

    def test_clean(self):
        self.list.clean()
        self.assertEqual(self.list.len(), 0)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_clean_one(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(1))
        list1.clean()
        self.assertEqual(list1.len(), 0)
        self.assertIsNone(list1.head)
        self.assertIsNone(list1.tail)

    def test_clean_empty(self):
        list1 = LinkedList2()
        list1.clean()
        self.assertEqual(list1.len(), 0)
        self.assertIsNone(list1.head)
        self.assertIsNone(list1.tail)

    def test_insert_to_empty(self):
        list1 = LinkedList2()
        list1.insert(None, Node(5))
        self.assertEqual(list1.len(), 1)
        self.assertEqual(list1.head.value, 5)
        self.assertEqual(list1.tail.value, 5)

    def test_insert_to_one(self):
        list1 = LinkedList2()
        node1 = Node(5)
        list1.add_in_tail(node1)
        list1.insert(node1, Node(7))
        self.assertEqual(list1.len(), 2)
        self.assertEqual(list1.head.value, 5)
        self.assertEqual(list1.tail.value, 7)

    def test_insert_to_one_as_tail(self):
        list1 = LinkedList2()
        node1 = Node(5)
        list1.add_in_tail(node1)
        list1.insert(None, Node(7))
        self.assertEqual(list1.len(), 2)
        self.assertEqual(list1.head.value, 5)
        self.assertEqual(list1.tail.value, 7)

    def test_insert_to_many_to_mid(self):
        node = self.list.find(3)
        self.list.insert(node, Node(7))
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.next.next.next.value, 7)
        self.assertEqual(self.list.head.next.next.next.value, 7)
        self.assertEqual(self.list.head.next.next.next.next.value, 4)

    def test_insert_to_many_after_none(self):
        self.list.insert(None, Node(7))
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 1)
        self.assertEqual(self.list.head.next.value, 2)
        self.assertEqual(self.list.tail.value, 7)
        self.assertEqual(self.list.tail.prev.value, 4)

    def test_insert_to_many_as_tail(self):
        self.list.insert(self.list.tail, Node(7))
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.tail.value, 7)

    def test_add_in_head_empty(self):
        list1 = LinkedList2()
        list1.add_in_head(Node(1))
        self.assertEqual(list1.len(), 1)
        self.assertEqual(list1.head.value, 1)
        self.assertIsNone(list1.head.prev)
        self.assertIsNone(list1.head.next)
        self.assertEqual(list1.tail.value, 1)
        self.assertIsNone(list1.tail.prev)
        self.assertIsNone(list1.tail.next)

    def test_add_in_head_one(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(1))
        list1.add_in_head(Node(5))
        self.assertEqual(list1.len(), 2)
        self.assertEqual(list1.head.value, 5)
        self.assertEqual(list1.head.next.value, 1)
        self.assertEqual(list1.tail.value, 1)

    def test_add_in_head_many(self):
        self.list.add_in_head(Node(55))
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.head.value, 55)
        self.assertEqual(self.list.tail.value, 4)