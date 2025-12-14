from unittest import TestCase

from ASD1.lesson09.task09 import NativeDictionary

class TestNativeDictionary(TestCase):
    def test_hash_fun(self):
        dict = NativeDictionary(17)
        self.assertEqual(dict.hash_fun('hash'), 7)
        self.assertEqual(dict.hash_fun('hash ok'), 7)

    def test_put_new(self):
        dict = NativeDictionary(17)
        dict.put('hash', 10)
        dict.put('hash ok', 100)
        self.assertEqual(10, dict.values[7])
        self.assertEqual('hash', dict.slots[7])
        self.assertEqual(100, dict.values[10])
        self.assertEqual('hash ok', dict.slots[10])
        self.assertEqual(dict.get('hash'), 10)

    def test_put_exists(self):
        dict = NativeDictionary(17)
        dict.put('hash', 10)
        dict.put('hash ok', 100)
        self.assertEqual(10, dict.values[7])
        self.assertEqual('hash', dict.slots[7])
        self.assertEqual(100, dict.values[10])

        dict.put('hash', 11)
        dict.put('hash ok', 111)
        self.assertEqual(11, dict.values[7])
        self.assertEqual('hash', dict.slots[7])
        self.assertEqual(111, dict.values[10])
        self.assertEqual('hash ok', dict.slots[10])

    def test_is_key_exists(self):
        dict = NativeDictionary(17)
        dict.put('hash', 10)
        dict.put('10', 100)
        self.assertTrue(dict.is_key('hash'))
        self.assertTrue(dict.is_key('10'))

    def test_is_key_not_exists(self):
        dict = NativeDictionary(17)
        dict.put('hash', 10)
        dict.put('10', 100)
        self.assertFalse(dict.is_key('hash ok'))
        self.assertFalse(dict.is_key('01'))

    def test_get_exists(self):
        dict = NativeDictionary(17)
        dict.put('hash', 10)
        self.assertEqual(dict.get('hash'), 10)
        dict.put('hash ok', 100)
        self.assertEqual(dict.get('hash'), 10)
        self.assertEqual(dict.get('hash ok'), 100)
        dict.put('hash ok', 111)
        self.assertEqual(dict.get('hash'), 10)
        self.assertEqual(dict.get('hash ok'), 111)

    def test_get_not_exists(self):
        dict = NativeDictionary(17)
        dict.put('hash', 10)
        self.assertEqual(dict.get('hash'), 10)
        self.assertIsNone(dict.get('hash ok'))
        dict.put('hash ok', 100)
        self.assertEqual(dict.get('hash'), 10)
        self.assertEqual(dict.get('hash ok'), 100)
        self.assertIsNone(dict.get('10'))