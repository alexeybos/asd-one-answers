# 3. Динамические массивы
# 3.5.* Реализуйте динамический массив на основе банковского метода.
# Сам по себе банковский метод оценки не дает прироста производительности, соответственно применение классического метода оценки дает O(n) в худшем
import ctypes

class BankDynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.bank = 0
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        # Тратим сэкономленное
        if new_capacity > self.capacity:
            self.bank -= new_capacity - self.capacity
        else:
            self.bank -= int((self.capacity - new_capacity) * 0.1)
        self.array = new_array
        self.capacity = new_capacity


    def append(self, itm):
        # ресайз делаем также по факту полной заполненности массива. Хотя можно, например, по определенному порогу в self.bank
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        else:
            self.bank += 2  # откладываем на реаллокацию
        self.array[self.count] = itm
        self.count += 1


    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count >= self.capacity:
            self.resize(2 * self.capacity)
        else:
            self.bank += 1  # откладываем на реаллокацию
        for ind in range(self.count, i, -1):
            self.array[ind] = self.array[ind - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        if self.count <= self.capacity / 2 and self.capacity > 16:
            self.resize(max(16, int(self.capacity / 1.5)))
        else:
            self.bank += 1  # откладываем на реаллокацию
        for ind in range(i, self.count - 1):
            self.array[ind] = self.array[ind + 1]
        self.count -= 1

# 3. Динамические массивы
# 3.6.* Реализуйте многомерный динамический массив: произвольное количество измерений, при этом каждое измерение может внутри масштабироваться по потребности.
# В конструкторе задаётся число измерений и размер по каждому из них. Обращаться к такому массиву надо как к обычному многомерному, например: myArr[1,2,3].
# Оценка основных методов также как и в одномерном динамическом массиве - O(n)
import ctypes


class MultyDynArray:
    def __init__(self, dimensions, *capacities):
        self.dimensions = dimensions
        self.capacities = capacities
        self.array = self.make_array(self.capacities)

    def __getitem__(self, indices):
        if self.is_out_of_bounds(indices):
            raise IndexError('Index is out of bounds')
        return self.array[self.get_real_index(*indices)]

    def __setitem__(self, indices, val):
        # проверка на расширение
        if self.is_out_of_bounds(indices):
            new_capacities = []
            i = 0
            for index in reversed(indices):
                if index >= self.capacities[i]:
                    new_capacities.append(index + 1)
                else:
                    new_capacities.append(self.capacities[i])
                i += 1
            self.resize(tuple(new_capacities))
        # вставка
        self.array[self.get_real_index(*indices)] = val

    def is_out_of_bounds(self, indices):
        i = 0
        for index in reversed(indices):
            if index < 0 or index >= self.capacities[i]:
                return True
            i += 1
        return False

    def get_real_index(self, *indices):
        index = 0
        dim_capacity_multiplier = 1
        current_dimension = 0
        for i in reversed(indices):
            index += i * dim_capacity_multiplier
            dim_capacity_multiplier = self.dim_full_capacity[current_dimension]
            current_dimension += 1
        return index

    def get_real_level_capacity(self, *capacities):
        result = []
        calc_capacity = 1
        for cap in capacities:
            calc_capacity *= cap
            result.append(calc_capacity)
        return result

    def make_array(self, new_capacities):
        summary_capacity = 1
        caps = new_capacities
        for i in caps:
            summary_capacity *= i
        arr = (summary_capacity * ctypes.py_object)()
        for i in range(summary_capacity):
            arr[i] = None
        self.dim_full_capacity = self.get_real_level_capacity(*new_capacities)
        return arr

    def resize(self, new_capacities):
        new_array = self.make_array(new_capacities)
        # copy (маппим старые индексы в новые)
        for i in range(len(self.array)):
            if self.array[i] is not None:
                indices = self.retain_indices(i)
                new_index = self.get_real_index(*indices)
                new_array[new_index] = self.array[i]
        self.capacities = new_capacities
        self.array = new_array

    def retain_indices(self, index):
        result = []
        rest_count = index
        for c in self.capacities:
            result.append(rest_count % c)
            rest_count = rest_count // c
        return tuple(reversed(result))

# Рефлексия по эталонному решению:
# 1. Связанный (связный) список
# 1.8. функцию поэлементного сложения двух одинаковых по размеру списков
# сложность (обе): O(n)
# Основные рекомендации соблюдены (сначала проверка длин, в цикле проверка только одного списка), но:
# 1. При неравенстве списков выбрасывается не исключение, а возвращается пустой список - не очень логичное поведение
# 2. Сейчас даже не могу сказать, зачем я в первоначальную проверку длин засунул list1.len() == 0
# Она просто лишняя и забирает дополнительные ресурсы. (Специально слазил в решение с первого прохождения курса - там я такую глупую проверку не добавлял :)