from unittest import TestCase

from ASD1.lesson04.task04 import Stack

class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(11)
        self.assertEqual(11, stack.stack[0])
        stack.push(22)
        self.assertEqual(22, stack.stack[1])
        stack.push(33)
        self.assertEqual(33, stack.stack[2])

    def test_size(self):
        stack = Stack()
        stack.push(11)
        self.assertEqual(1, stack.size())
        stack.push(12)
        self.assertEqual(2, stack.size())
        stack.push(13)
        self.assertEqual(3, stack.size())

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(11)
        self.assertEqual(1, stack.size())
        self.assertEqual(11, stack.peek())
        stack.push(12)
        self.assertEqual(2, stack.size())
        self.assertEqual(12, stack.peek())
        stack.push(13)
        self.assertEqual(3, stack.size())
        self.assertEqual(13, stack.peek())

    def test_pop(self):
        stack = Stack()
        stack.push(11)
        stack.push(12)
        stack.push(13)
        self.assertEqual(13, stack.pop())
        self.assertEqual(12, stack.pop())
        self.assertEqual(11, stack.pop())
        self.assertIsNone(stack.pop())
        self.assertIsNone(stack.peek())

