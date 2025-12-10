# 8. Хэширование
# 3.* Реализуйте динамическую хэш-таблицу
# Сложность (при ресайзе таблицы) временная O(n) и пространственная O(n) из-за необходимости сохранить имеющиеся значения для перехеширования
class DynHashTable():
    def __init__(self):
        self.capacity = 16
        self.step = 3
        self.count = 0
        self.slots = DynArray()
        for i in range(self.slots.capacity):
            self.slots.append(None)

    def hash_fun(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return sum % self.capacity

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        i = 0
        while i < self.step:
            if self.slots[slot] is None:
                return slot
            slot += self.step
            if slot >= self.capacity:
                slot -= self.capacity
                i += 1
        return None

    def put(self, value):
        self.__resize_if_need()
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            self.count += 1
        return slot

    def find(self, value):
        slot = self.hash_fun(value)
        i = 0
        if slot is None:
            return None
        while i < self.step:
            if self.slots[slot] == value:
                return slot
            slot += self.step
            if slot >= self.capacity:
                slot -= self.capacity
                i += 1
        return None

    def __resize_if_need(self):
        if (self.count + 1) / self.capacity < 0.75:
            return
        tmp_table = []
        new_capacity = self.capacity * 2
        self.slots.resize(new_capacity)
        for i in range(self.capacity):
            tmp_table.append(self.slots[i])
            self.slots[i] = None
        for i in range(self.capacity, new_capacity):
            self.slots.append(None)
        self.capacity = new_capacity
        # делаю rehash
        self.count = 0
        for el in tmp_table:
            if el is not None:
                self.put(el)

# 8. Хэширование
# 4.* Реализуйте хэш-таблицу, которая использует несколько хэш-функций для каждой операции вставки, чтобы уменьшить вероятность коллизий.
# вероятность коллизий уменьшается, время вставки (поиска) практически не увеличивается (но зависит от сложности хзш-функции).
class MultiHashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.hashes = []
        self.hashes[0] = lambda val: self.hash_fun1(val)
        self.hashes[1] = lambda val: self.hash_fun2(val)
        self.hashes[2] = lambda val: self.hash_fun3(val)

    def hash_fun1(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return sum % 17

    def hash_fun2(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return ((11 * sum + 90) % 97) % 17

    def hash_fun3(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return ((23 * sum + 53) % 79) % 17

    def seek_slot(self, value, search_val):
        slot = None
        for i in range(3):
            slot = self.hashes[i](value)
            if self.slots[slot] == search_val:
                return slot
        i = 0
        while i < self.step:
            if self.slots[slot] == search_val:
                return slot
            slot += self.step
            if slot >= self.size:
                slot -= self.size
                i += 1
        return None

    def put(self, value):
        slot = self.seek_slot(value, None)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value):
        slot = self.seek_slot(value, value)
        return slot

# 8. Хэширование
# 5.* Организуйте ddos-атаку на вашу исходную хэш-таблицу -- с помощью специально сгенерированных ключей, вызывающих большое число коллизий.
# Затем модифицируйте хэш-таблицу для защиты от таких атак (например, посолите).
# Использовал динамическую соль.
import random

class SaltHashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.collision_cnt = 0
        self.salt = {}

    def hash_fun(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return ((23 * sum + 53) % 79) % 17

    def seek_slot(self, value, search_val):
        slot = self.hash_fun(value)
        i = 0
        while i < self.step:
            if self.slots[slot] == search_val:
                return slot
            slot += self.step
            if search_val is None:
                self.collision_cnt += 1
            if slot >= self.size:
                slot -= self.size
                i += 1
        return None

    def get_salt_value(self, value):
        salt = self.salt.get(value)
        if salt is None:
            salt = value + 'salt frase' + str(random.randint(0, 100000000))
            self.salt.update({value: salt})
        return salt

    def put(self, value):
        salt_val = self.get_salt_value(value)
        slot = self.seek_slot(salt_val, None)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value):
        salt_val = self.get_salt_value(value)
        slot = self.seek_slot(salt_val, salt_val)
        return slot

# Рефлексия по эталонным решениям предыдущих заданий:
# 6. Двусторонняя очередь (deque)
#  7.3.* Напишите функцию, которая с помощью deque проверяет, является ли некоторая строка палиндромом
# Реализовано согласно рекомендациям - заполняю деку, потом с обоих сторон убираю, сравнивая

# 7.4.* Напишите метод, который возвращает минимальный элемент деки за O(1).
# Здесь уже большая разница между моей и рекомендованной реализацией. У меня реализация через два стека, по сути имитирующих два конца деки
# В целом алгоритм тоже рабочий, но производительность кажется будет хуже (особенно в случае если добавление будет идти всегда в один конец, а удаление из другого)
# Да и в общем алгоритм с декой выглядит проще понятней.

# 7.5.* Реализуйте двустороннюю очередь с помощью динамического массива.
# Методы добавления и удаления элементов с обоих концов деки должны работать за амортизированное время o(1).
# Реализовано как и рекомендовано - через композицию. Единственно упомяну, что перед расширением обрабатываю массив из-за того,
# что указатели на голову и конец деки могут быть смещены относительно реальных индексов массива и для корректной его реаллокации
# необходимо чтобы tail указывал на 0
