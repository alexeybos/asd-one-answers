# 10. Множества
# 4.* Добавьте метод, реализующий декартово произведение множеств
# Сложность временная и пространственная O(n^2)
def cartesian(self, set2: PowerSet) -> PowerSet:
    result = PowerSet()
    for key in self._set:
        for key2 in set2._set:
            result.put((key,key2))
    return result

# 10. Множества
# 5.* Напишите функцию, которая находит пересечение любых трёх и более множеств (принимает количество множеств >= 3 в качестве списка).
# Сложность временная и пространственная O(n)
def intersect_all(sets) -> PowerSet:
    result = copy.deepcopy(sets[0])
    for i in range(1, len(sets)):
        result = result.intersection(sets[i])
    return result

# 10. Множества
# 6.* Реализуйте мульти-множество (Bag), в котором каждый элемент может присутствовать несколько раз.
# Добавьте методы добавления элементов, удаления одного экземпляра элемента и получения списка всех элементов с их частотами (сколько раз встречаются).
class Bag:
    def __init__(self):
        self._data = {}
        self._size = 0

    def put(self, key, freq = 1):
        if key in self._data:
            self._data[key] = self._data[key] + freq
        else:
            self._data[key] = freq
        self._size += freq

    def remove_first(self, key):
        if key in self._data:
            self._size -= 1
        if key in self._data and self._data[key] > 1:
            self._data[key] = self._data[key] - 1
        else:
            self._data.pop(key)

    def get_elements_with_freq(self):
        return self._data

    def get(self, value: Any) -> bool :
        return self._data.get(value, 0) > 0

    def get_freq(self, value: Any) -> bool :
        return self._data.get(value, 0)

    def size(self) -> int:
        return int(self._size)

    def intersection(self, set2: Bag) -> Bag:
        result = Bag()
        for key in self._data:
            freq = set2.get_freq(key)
            if freq > 0:
                result.put(key, min(self._data[key], freq))
        return result

    def union(self, set2: Bag) -> Bag:
        result = Bag()
        for key in self._data:
            result.put(key, self._data[key])
        for key in set2._data:
            result.put(key, set2._data[key])
        return result

    def difference(self, set2: Bag) -> Bag:
        result = Bag()
        for key in self._data:
            freq = set2.get_freq(key)
            if freq < self._data[key]:
                result.put(key, self._data[key] - freq)
        return result

    def issubset(self, set2: Bag) -> bool:
        diff = set2.difference(self)
        return diff.size() == 0

    def equals(self, set2: Bag) -> bool:
        diff = set2.difference(self)
        return diff.size() == 0

# Рефлексия по эталонным решениям предыдущих заданий:
# 8. Хэширование
# 3.* Реализуйте динамическую хэш-таблицу
# Забыл про геттер размера буфера - момент ресайза определяю по самостоятельно подсчитываемым переменным внутри класса (т.е. даже не по незакрытым полям динамического массива), что конечно в корне не верно.
# В остальном реализовано согласно рекомендациям - композиция с динамическим массивом, вызов метода ресайза у массива и перераспределение значений в увеличенном массиве.

# 8. Хэширование
# 5.* Модифицируйте хэш-таблицу для защиты от таких атак (например, посолите).
# А здесь я свою ошибку первого прохождения курса хорошо запомнил (тогда использовал статическую соль). В этот раз сделал сразу верно - использовал динамическую соль.