from unittest import TestCase

from ASD1.lesson11.task11 import BloomFilter

class TestBloomFilter(TestCase):
    def test_is_value(self):
        bfilter = BloomFilter(32)
        bfilter.add("0123456789")
        bfilter.add("1234567890")
        bfilter.add("2345678901")
        bfilter.add("3456789012")
        bfilter.add("4567890123")
        bfilter.add("5678901234")
        bfilter.add("6789012345")
        bfilter.add("7890123456")
        bfilter.add("8901234567")
        bfilter.add("9012345678")
        self.assertTrue(bfilter.is_value("0123456789"))
        self.assertTrue(bfilter.is_value("1234567890"))
        self.assertTrue(bfilter.is_value("2345678901"))
        self.assertTrue(bfilter.is_value("3456789012"))
        self.assertTrue(bfilter.is_value("4567890123"))
        self.assertTrue(bfilter.is_value("5678901234"))
        self.assertTrue(bfilter.is_value("6789012345"))
        self.assertTrue(bfilter.is_value("7890123456"))
        self.assertTrue(bfilter.is_value("8901234567"))
        self.assertTrue(bfilter.is_value("9012345678"))
        self.assertFalse(bfilter.is_value("01234a6789"))

