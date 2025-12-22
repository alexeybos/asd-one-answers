# 11. Фильтр Блюма
# 2.* Напишите алгоритм слияния нескольких фильтров Блюма (одинакового размера и с одинаковым набором хэш-функций).
# Как изменится вероятность ложного срабатывания для итогового фильтра?
# Если длина и набор хеш-функций одинаковый, то слияние нескольких фильтров Блюма заключается в простой операции
# "логического или" над битовыми массивами фильтров. Согласно формуле расчета вероятности ложного срабатывания (0,6931^(m/n)),
# при слиянии у нас растет n, значит растет и вероятность ложного срабатывания.

# 3.* Реализуйте фильтр Блюма, предусматривающий удаление элементов (стандартный фильтр Блюма удаление не поддерживает).
# Учтите, что при удалении несуществующих элементов (с ложноположительным результатом проверки их наличия) структура фильтра нарушается и могут
# удаляться другие входные значения.
from ASD1.test.lesson10.bag import Bag
class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bloom = int(2 << (f_len - 1))
        self.counter = Bag()

    def delete(self, str1):
        index1 = 1 << self.hash1(str1)
        index2 = 1 << self.hash2(str1)
        self.counter.remove_first(index1)
        self.counter.remove_first(index2)
        if self.counter.get_freq(index1) < 1 and self.counter.get_freq(index2) < 1:
            self.bloom = self.bloom & ~index1
            self.bloom = self.bloom & ~index2

    def hash1(self, str1):
        prev_res = 0
        for c in str1:
            code = ord(c)
            prev_res = (prev_res * 17 + code) % self.filter_len
        return prev_res

    def hash2(self, str1):
        prev_res = 0
        for c in str1:
            code = ord(c)
            prev_res = (prev_res * 223 + code) % self.filter_len
        return prev_res

    def add(self, str1):
        index1 = 1 << self.hash1(str1)
        index2 = 1 << self.hash2(str1)
        self.bloom = self.bloom | index1
        self.bloom = self.bloom | index2
        self.counter.put(index1)
        self.counter.put(index2)

    def is_value(self, str1):
        index1 = 1 << self.hash1(str1)
        index2 = 1 << self.hash2(str1)
        return ((self.bloom & index1) == index1) and ((self.bloom & index2) == index2)

# 4.* Подумайте (и попробуйте реализовать), каким может быть алгоритм, который анализирует конфигурацию фильтра Блюма и пытается, насколько возможно,
# восстановить исходное множество с учётом всех ограничений и искажений (например, коллизий, ложноположительных срабатываний...).
# Под исходным множеством понимаются исходные данные, оригинальное множество элементов, которые были добавлены в фильтр Блюма через метод Add.
# Попробовал подобрать брутфорсом с ограничениями "только цифры, длина строки 10". Совпадений не получилось.
# Можно наверное сделать ограничения "по словарю" или какие-нибудь другие дополнительные ограничения, позволяющие сузить поиск значений.
    def test_bloom_recovery(self):
        bfilter = BloomFilter(32)
        bfilter.add("0123456789")
        bfilter.add("2345678901")
        bfilter.add("4567890123")
        bfilter.add("6789012345")
        bfilter.add("8901234567")

        bloom_real = bin(bfilter.bloom)
        eq = False
        interation = 0
        bfilter_new = BloomFilter(32)
        vals = []
        while (not eq) and (interation < 100000):
            vals = []
            i = 0
            while i < 5:
                str1 = ''
                for j in range(10):
                    str1 = str1 + str(random.randint(0, 9))
                if bfilter.is_value(str1):
                    i = i + 1
                    bfilter_new.add(str1)
                    vals.append(str1)
            eq = bloom_real == bin(bfilter_new.bloom)
            interation = interation + 1
        print(eq)
        print(interation)
        for v in vals:
            print(v)

# Рефлексия по эталонным решениям предыдущих заданий:
# 9. Ассоциативный массив
# 5.* Реализуйте словарь с использованием упорядоченного списка по ключу для оптимизации производительности поиска.
# Разделение по хранилищам сделано согласно рекомендации, но вот сохранение в моем варианте происходит гораздо "тяжелее":
# значение в массив значений не добавляется, а вставляется в индекс ключа. Таким образом мы дополнительно получаем
# накладные расходы при смещении элементов в массиве значений словаря. До кортежа key-value_index я не додумался.