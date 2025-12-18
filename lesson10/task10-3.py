import time
from unittest import TestCase

from ASD1.lesson10.task10 import PowerSet

class TestPowerSet(TestCase):
    def test_put_size(self):
        my_set = PowerSet()
        my_set.put('qw')
        self.assertEqual(my_set.size(), 1)
        self.assertTrue(my_set.get('qw'))
        self.assertFalse(my_set.remove('qwq'))
        my_set.put('qw')
        self.assertEqual(my_set.size(), 1)
        my_set.put(12)
        self.assertEqual(my_set.size(), 2)

    def test_remove(self):
        my_set = PowerSet()
        my_set.put('qw')
        my_set.put(123)
        self.assertEqual(my_set.size(), 2)
        self.assertFalse(my_set.remove('q'))
        self.assertTrue(my_set.remove('qw'))
        self.assertEqual(my_set.size(), 1)
        self.assertFalse(my_set.get('qw'))
        self.assertFalse(my_set.remove('qw'))
        self.assertFalse(my_set.remove(12))
        self.assertTrue(my_set.remove(123))
        self.assertEqual(my_set.size(), 0)
        self.assertFalse(my_set.remove('qw'))

    # - пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества;
    def test_intersection_to_empty(self):
        my_set1 = PowerSet()
        my_set1.put('qw')
        my_set1.put('qwqw')
        my_set1.put(123)

        my_set2 = PowerSet()
        my_set2.put('dfdss')
        my_set2.put('dfdss2')
        self.assertEqual(0, my_set1.intersection(my_set2).size())

    def test_intersection_to_not_empty(self):
        my_set1 = PowerSet()
        my_set1.put('qw')
        my_set1.put('qwqw')
        my_set1.put(123)

        my_set2 = PowerSet()
        my_set2.put('dfdss')
        my_set2.put(123)
        my_set2.put('dfdss2')
        my_set2.put('meow')
        res = my_set1.intersection(my_set2)
        self.assertEqual(1, res.size())
        self.assertTrue(res.get(123))

    # - объединение union(), когда оба параметра непустые, и когда один из параметров -- пустое множество;
    def test_union_with_empty(self):
        my_set1 = PowerSet()
        my_set1.put('meow')
        my_set1.put(123)
        my_set1.put('qw')
        my_set2 = PowerSet()
        res = my_set1.union(my_set2)
        self.assertEqual(3, res.size())
        self.assertTrue(res.get(123))
        self.assertTrue(res.get('meow'))
        self.assertTrue(res.get('qw'))

        res = my_set2.union(my_set1)
        self.assertEqual(3, res.size())
        self.assertTrue(res.get(123))
        self.assertTrue(res.get('meow'))
        self.assertTrue(res.get('qw'))

    def test_union(self):
        my_set1 = PowerSet()
        my_set1.put('meow')
        my_set1.put(123)
        my_set1.put('qw')
        my_set2 = PowerSet()
        my_set2.put('dfdss')
        my_set2.put(123)
        my_set2.put('dfdss2')
        res = my_set1.union(my_set2)
        self.assertEqual(5, res.size())
        self.assertTrue(res.get(123))
        self.assertTrue(res.get('meow'))
        self.assertTrue(res.get('qw'))
        self.assertTrue(res.get('dfdss'))
        self.assertTrue(res.get('dfdss2'))

    # - разница difference(), чтобы в результате получались как пустое, так и непустое множества;
    def test_difference(self):
        my_set1 = PowerSet()
        my_set1.put('qw')
        my_set1.put('qwqw')
        my_set1.put(123)

        my_set2 = PowerSet()
        my_set2.put('dfdss')
        my_set2.put(123)
        my_set2.put('dfdss2')
        my_set2.put('meow')
        res = my_set1.difference(my_set2)
        self.assertEqual(2, res.size())
        self.assertTrue(res.get('qw'))
        self.assertTrue(res.get('qwqw'))

        res = my_set2.difference(my_set1)
        self.assertEqual(3, res.size())
        self.assertTrue(res.get('dfdss'))
        self.assertTrue(res.get('dfdss2'))
        self.assertTrue(res.get('meow'))

    def test_difference_to_empty(self):
        my_set1 = PowerSet()
        my_set1.put('meow')
        my_set1.put(123)

        my_set2 = PowerSet()
        my_set2.put('dfdss')
        my_set2.put(123)
        my_set2.put('dfdss2')
        my_set2.put('meow')
        res = my_set1.difference(my_set2)
        self.assertEqual(0, res.size())

    # - подмножество issubset() -- рассмотрите три случая (все элементы параметра входят в текущее множество, все элементы текущего множества входят в параметр, не все элементы параметра входят в текущее множество);
    def test_issubset_param_full_in_set(self):
        my_set1 = PowerSet()
        my_set1.put('meow')
        my_set1.put(123)

        my_set2 = PowerSet()
        my_set2.put('dfdss')
        my_set2.put(123)
        my_set2.put('dfdss2')
        my_set2.put('meow')

        self.assertTrue(my_set2.issubset(my_set1))

    def test_issubset_set_full_in_param(self):
        my_set1 = PowerSet()
        my_set1.put('meow')
        my_set1.put(123)

        my_set2 = PowerSet()
        my_set2.put(123)
        my_set2.put('meow')
        self.assertTrue(my_set2.issubset(my_set1))
        self.assertTrue(my_set1.issubset(my_set2))
        my_set2.put('dfdss')

        self.assertFalse(my_set1.issubset(my_set2))

    def test_issubset_param_not_full_in_set(self):
        my_set1 = PowerSet()
        my_set1.put('meow')
        my_set1.put(123)
        my_set1.put('123')

        my_set2 = PowerSet()
        my_set2.put(123)
        my_set2.put('meow')
        my_set2.put('dfdss')
        my_set2.put('dfd')

        self.assertFalse(my_set1.issubset(my_set2))
        self.assertFalse(my_set2.issubset(my_set1))

    # - равенство equals() -- проверка, равно ли текущее множество параметру;
    def test_equals(self):
        my_set1 = PowerSet()
        my_set2 = PowerSet()
        self.assertTrue(my_set1.equals(my_set2))
        self.assertTrue(my_set2.equals(my_set1))
        my_set1.put('q')
        my_set1.put('qw')
        self.assertFalse(my_set1.equals(my_set2))
        self.assertFalse(my_set2.equals(my_set1))
        my_set2.put('q')
        self.assertFalse(my_set1.equals(my_set2))
        self.assertFalse(my_set2.equals(my_set1))
        my_set2.put('qw')
        self.assertTrue(my_set1.equals(my_set2))
        self.assertTrue(my_set2.equals(my_set1))
        my_set1.put(123)
        self.assertFalse(my_set1.equals(my_set2))
        self.assertFalse(my_set2.equals(my_set1))

    # -- быстродействие (операции над множествами из десятков тысяч элементов укладываются в пару секунд).
    def test_speed(self):
        my_set = PowerSet()
        start = time.time()  ## точка отсчета времени
        for i in range(30000):
            my_set.put(i)
        for i in range(30000):
            my_set.get(i)
        for i in range(30000):
            my_set.remove(i)
        end = time.time() - start
        print(end)  ## вывод времени
        my_set = None
        my_set1 = PowerSet()
        my_set2 = PowerSet()
        for i in range(30000):
            my_set1.put(i)
        for i in range(30000, 60000):
            my_set2.put(i)
        self.assertEqual(my_set1.size(), my_set2.size())
        start = time.time()  ## точка отсчета времени
        # intersection
        res = my_set1.intersection(my_set2)
        end = time.time() - start
        print(end)

        start = time.time()  ## точка отсчета времени
        # union
        res = my_set1.union(my_set2)
        end = time.time() - start
        print(end)

        start = time.time()  ## точка отсчета времени
        # difference
        res = my_set1.difference(my_set2)
        end = time.time() - start
        print(end)

        start = time.time()  ## точка отсчета времени
        #test_equals
        result = my_set1.equals(my_set2)
        end = time.time() - start
        print(end)

        start = time.time()  ## точка отсчета времени
        # issubset
        res = my_set1.issubset(my_set2)
        end = time.time() - start
        print(end)
