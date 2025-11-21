from unittest import TestCase
from ASD1.lesson03.task03 import DynArray

class TestDynArray(TestCase):
    def test_insert_empty(self):
        arr = DynArray()
        arr.insert(0, 100)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(100, arr[0])
        self.assertEqual(1, len(arr))

    def test_insert_first(self):
        arr = DynArray()
        arr.append(100)
        arr.append(200)
        arr.append(300)
        arr.insert(0, 400)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(400, arr[0])
        self.assertEqual(100, arr[1])
        self.assertEqual(200, arr[2])
        self.assertEqual(300, arr[3])
        self.assertEqual(4, len(arr))

    def test_insert_last_no_extend(self):
        arr = DynArray()
        arr.append(100)
        arr.append(200)
        arr.append(300)
        arr.insert(3, 400)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(100, arr[0])
        self.assertEqual(200, arr[1])
        self.assertEqual(300, arr[2])
        self.assertEqual(400, arr[3])
        self.assertEqual(4, len(arr))

    def test_insert_very_last_no_extend(self):
        arr = DynArray()
        for i in range(15):
            arr.append(i)
        arr.insert(15, 400)
        self.assertEqual(16, arr.capacity)
        for i in range(15):
            self.assertEqual(i, arr[i])
        self.assertEqual(400, arr[15])
        self.assertEqual(16, len(arr))

    def test_insert_last_with_extend(self):
        arr = DynArray()
        for i in range(16):
            arr.append(i)
        arr.insert(16, 100)
        self.assertEqual(32, arr.capacity)
        self.assertEqual(100, arr[16])
        for i in range(16):
            self.assertEqual(i, arr[i])
        self.assertEqual(17, len(arr))

    def test_insert_mid_no_extend(self):
        arr = DynArray()
        arr.append(100)
        arr.append(200)
        arr.append(300)
        arr.insert(2, 400)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(100, arr[0])
        self.assertEqual(200, arr[1])
        self.assertEqual(400, arr[2])
        self.assertEqual(300, arr[3])
        self.assertEqual(4, len(arr))

    def test_insert_mid_with_extend(self):
        arr = DynArray()
        for i in range(16):
            arr.append(i)
        arr.insert(10, 100)
        self.assertEqual(32, arr.capacity)
        self.assertEqual(100, arr[10])
        self.assertEqual(0, arr[0])
        self.assertEqual(15, arr[16])
        self.assertEqual(17, len(arr))

    def test_insert_error(self):
        arr = DynArray()
        arr.append(100)
        arr.append(200)
        arr.append(300)
        with self.assertRaises(IndexError):
            arr.insert(4, 400)

# -- удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);
    # -- удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);
    def test_delete_error(self):
        arr = DynArray()
        arr.append(100)
        arr.append(200)
        with self.assertRaises(IndexError):
            arr.delete(2)

    def test_delete_empty_error(self):
        arr = DynArray()
        with self.assertRaises(IndexError):
            arr.delete(0)

    def test_delete_first(self):
        arr = DynArray()
        arr.append(100)
        arr.append(200)
        arr.delete(0)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(200, arr[0])
        self.assertEqual(1, len(arr))
        with self.assertRaises(IndexError):
            deleted = arr[1]

    def test_delete_tail(self):
        arr = DynArray()
        arr.append(100)
        arr.append(200)
        arr.delete(1)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(100, arr[0])
        self.assertEqual(1, len(arr))
        with self.assertRaises(IndexError):
            deleted = arr[1]

    def test_delete_last_to_empty(self):
        arr = DynArray()
        arr.append(100)
        arr.delete(0)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(0, len(arr))
        with self.assertRaises(IndexError):
            deleted = arr[0]

    def test_delete_mid(self):
        arr = DynArray()
        arr.append(100)
        arr.append(200)
        arr.append(300)
        arr.append(400)
        self.assertEqual(400, arr[3])
        arr.delete(2)
        self.assertEqual(16, arr.capacity)
        self.assertEqual(3, len(arr))
        self.assertEqual(100, arr[0])
        self.assertEqual(200, arr[1])
        self.assertEqual(400, arr[2])
        with self.assertRaises(IndexError):
            deleted = arr[3]

    def test_delete_with_shrink(self):
        arr = DynArray()
        for i in range(33):
            arr.append(i)
        arr.delete(16)
        for i in range(32):
            if i < 16:
                self.assertEqual(i, arr[i])
            else:
                self.assertEqual(i + 1, arr[i])
        self.assertEqual(32, len(arr))
        self.assertEqual(64, arr.capacity)
        arr.delete(10)
        self.assertEqual(31, len(arr))
        new_cap = int(64 / 1.5)
        self.assertEqual(new_cap, arr.capacity)


    def test_delete_with_shrink_to_less_16(self):
        arr = DynArray()
        for i in range(17):
            arr.append(i)
        self.assertEqual(32, arr.capacity)
        arr.delete(6)
        self.assertEqual(32, arr.capacity)
        arr.delete(6)
        self.assertEqual(21, arr.capacity)
        for i in range(5):
            arr.delete(i)
        self.assertEqual(10, len(arr))
        self.assertEqual(21, arr.capacity)
        arr.delete(6)
        self.assertEqual(16, arr.capacity)

