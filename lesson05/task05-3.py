from unittest import TestCase

from ASD1.lesson05.task05 import Queue

class TestQueue(TestCase):
    def test_size(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(2, q.size())

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue.queue[0])
        queue.enqueue(2)
        self.assertEqual(2, queue.size())
        self.assertEqual(2, queue.queue[0])
        self.assertEqual(1, queue.queue[1])
        queue.enqueue(3)
        self.assertEqual(3, queue.size())
        self.assertEqual(3, queue.queue[0])
        self.assertEqual(2, queue.queue[1])
        self.assertEqual(1, queue.queue[2])

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(1, queue.size())
        self.assertEqual(1, queue.queue[0])
        queue.enqueue(2)
        self.assertEqual(2, queue.size())
        self.assertEqual(2, queue.queue[0])
        self.assertEqual(1, queue.queue[1])
        queue.enqueue(3)
        self.assertEqual(3, queue.size())
        self.assertEqual(3, queue.queue[0])
        self.assertEqual(2, queue.queue[1])
        self.assertEqual(1, queue.queue[2])

        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.size())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(1, queue.size())
        self.assertEqual(3, queue.dequeue())
        self.assertEqual(0, queue.size())
        self.assertIsNone(queue.dequeue())
        self.assertEqual(0, queue.size())

