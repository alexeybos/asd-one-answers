from unittest import TestCase

from ASD1.lesson12.task12 import NativeCache

class TestNativeCache(TestCase):
    def test_put(self):
        cache = NativeCache(5)
        cache.put("1", "value1")
        self.assertEqual("value1", cache.values[4])
        cache.put("2", "value2")
        self.assertEqual("value2", cache.values[3])
        cache.put("3", "value3")
        self.assertEqual("value3", cache.values[1])
        cache.put("4", "value4")
        self.assertEqual("value4", cache.values[2])
        cache.put("5", "value5")
        cache.get("2")
        cache.get("5")
        cache.get("1")
        cache.get("4")
        self.assertEqual(2, cache.hits[0])
        self.assertEqual(1, cache.hits[1])
        self.assertEqual(2, cache.hits[2])
        self.assertEqual(2, cache.hits[3])
        self.assertEqual(2, cache.hits[4])
        cache.put("6", "value6")
        self.assertEqual("value6", cache.values[1])
        self.assertEqual(0, cache.hits[1])
