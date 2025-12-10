from unittest import TestCase

from ASD1.lesson08.task08 import HashTable

class TestHashTable(TestCase):
    def test_hash_fun(self):
        table1 = HashTable(17, 3)
        self.assertEqual(2, table1.hash_fun(''))
        self.assertEqual(4, table1.hash_fun('10'))
        self.assertEqual(4, table1.hash_fun('01'))
        self.assertEqual(7, table1.hash_fun('hash'))
        self.assertEqual(7, table1.hash_fun('hash ok'))

    def test_seek_slot(self):
        table1 = HashTable(17, 3)
        slot = 2
        for i in range(5):
            self.assertEqual(slot, table1.seek_slot(''))
            slot += 3
        slot = 0
        for i in range(6):
            self.assertEqual(slot, table1.seek_slot(''))
            slot += 3
        slot = 1
        for i in range(6):
            self.assertEqual(slot, table1.seek_slot(''))
            slot += 3
        self.assertIsNone(table1.seek_slot(''))

    def test_put(self):
        table1 = HashTable(17, 3)
        self.assertEqual(2, table1.put(''))
        self.assertEqual(4, table1.put('10'))
        self.assertEqual(7, table1.put('01'))
        self.assertEqual(10, table1.put('hash'))
        self.assertEqual(13, table1.put('hash ok'))

    def test_find(self):
        table1 = HashTable(17, 3)
        self.assertEqual(2, table1.put(''))
        self.assertEqual(4, table1.put('10'))
        self.assertEqual(7, table1.put('01'))
        self.assertEqual(10, table1.put('hash'))
        self.assertEqual(13, table1.put('hash ok'))

        self.assertEqual(2, table1.find(''))
        self.assertEqual(4, table1.find('10'))
        self.assertEqual(7, table1.find('01'))
        self.assertEqual(10, table1.find('hash'))
        self.assertEqual(13, table1.find('hash ok'))

        self.assertIsNone(table1.find('11'))