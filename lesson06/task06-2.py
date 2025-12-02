# 6. Двусторонняя очередь (deque)
# Нумерация заданий почему-то с 7, но оставил нумерацию как в тексте урока
#  7.3.* Напишите функцию, которая с помощью deque проверяет, является ли некоторая строка палиндромом (читается одинаково слева направо и справа налево).
# Сложность временная O(n) и пространственная O(n)
def is_palindrome(str_for_check) -> bool:
    deque = Deque()
    for char in str_for_check:
        if char.isalpha():
            deque.addFront(char.lower())
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True

# 6. Двусторонняя очередь (deque)
# 7.4.* Напишите метод, который возвращает минимальный элемент деки за O(1).
class MinDeque(Deque):
    def __init__(self):
        super().__init__()
        self.min_head = Stack()
        self.min_tail = Stack()

    # Сам метод получения min
    def get_min(self):
        if self.min_tail.size() == 0 and self.min_head.size() == 0:
            return None
        elif self.min_tail.size() == 0:
            return self.min_head.peek()
        elif self.min_head.size() == 0:
            return self.min_tail.peek()
        val_min_head = self.min_head.peek()
        val_min_tail = self.min_tail.peek()
        return min(val_min_head, val_min_tail)

    def remove_min(self, val, stack1: Stack, stack2: Stack):
        if stack1.size() > 0 and stack1.peek() == val:
            return stack1.pop()
        while stack2.size() > 0 and stack2.peek() >= val:
            stack1.push(stack2.pop())
        return stack1.pop()

    def addFront(self, item):
        if self.min_head.size() == 0 or item <= self.min_head.peek():
            self.min_head.push(item)
        super().addFront(item)

    def addTail(self, item):
        if self.min_tail.size() == 0 or item <= self.min_tail.peek():
            self.min_tail.push(item)
        super().addTail(item)

    def removeFront(self):
        val = super().removeFront()
        if val is not None:
            self.remove_min(val, self.min_head, self.min_tail)
        return val

    def removeTail(self):
        val = super().removeTail()
        if val is not None:
            self.remove_min(val, self.min_tail, self.min_head)
        return val

# 6. Двусторонняя очередь (deque)
# 7.5.* Реализуйте двустороннюю очередь с помощью динамического массива. Методы добавления и удаления элементов с обоих концов деки должны работать за амортизированное время o(1).
class DynArrayDeque:
    def __init__(self):
        self.arr = DynArray()
        self.count = 0
        self.head = None
        self.tail = None
        for i in range(self.arr.capacity):
            self.arr.append(None)

    def addFront(self, item):
        index_for_ins = self.__move_index_right(self.head)
        if index_for_ins == self.tail:
            self.resize_array()
            index_for_ins = self.head
        if self.tail is None:
            self.tail = 0
        self.count += 1
        self.arr.array[index_for_ins] = item
        self.head = index_for_ins

    def addTail(self, item):
        index_for_ins = self.__move_index_left(self.tail)
        if index_for_ins == self.head:
            self.resize_array()
            index_for_ins = self.tail
        if self.head is None:
            self.head = 0
        self.count += 1
        self.arr.array[index_for_ins] = item
        self.tail = index_for_ins

    def removeFront(self):
        if self.size() == 0:
            return None
        self.count -= 1
        val = self.arr.array[self.head]
        self.arr.array[self.head] = None
        self.head = self.__move_index_left(self.head)
        if self.size() == 0:
            self.head = None
            self.tail = None
        return val

    def removeTail(self):
        if self.size() == 0:
            return None
        self.count -= 1
        val = self.arr.array[self.tail]
        self.arr.array[self.tail] = None
        self.tail = self.__move_index_right(self.tail)
        if self.size() == 0:
            self.head = None
            self.tail = None
        return val

    def size(self):
        return self.count

    def __move_index_right(self, index_for_move):
        if index_for_move is None or index_for_move + 1 == self.arr.capacity:
            return 0
        return index_for_move + 1

    def __move_index_left(self, index_for_move):
        if index_for_move is None:
            return 0
        if index_for_move == 0:
            return self.arr.capacity - 1
        return index_for_move - 1

    def resize_array(self):
        real_deque = []
        index = self.tail
        for i in range(self.arr.capacity):
            real_deque.append(self.arr[index])
            index = self.__move_index_right(index)
        for i in range(self.arr.capacity):
            self.arr.array[i] = real_deque[i]
        self.arr.append(None)
        for i in range(self.count, self.arr.capacity):
            self.arr.array[i] = None
        self.head = self.count - 1
        self.tail = 0

# 6. Двусторонняя очередь (deque)
# 7.6.* Напишите автономную функцию, которая проверяет баланс скобок в символьном выражении. Внутри этой функции используйте стек.
# Алгоритм должен работать за O(N)
def is_parenthesis_balanced(str_for_check) -> bool:
    stack = Stack()
    dct = {'(': ')', '[': ']', '{': '}'}
    is_bracket_equal = True
    for char in str_for_check:
        if char in dct.keys():
            stack.push(dct.get(char))
        elif char in dct.values():
            is_bracket_equal = stack.pop() == char
        if not is_bracket_equal:
            return False
    return stack.size() == 0

# Рефлексия по эталонным решениям предыдущих заданий:
# 4. Стек
# 5.* Напишите функцию, которая проверяет сбалансированность открывающих и закрывающих скобок
# 6.* Расширьте функцию проверки сбалансированности скобок, если скобки могут быть трех типов: (), {}, [].
# Алгоритм реализован с учетом всех рекомендаций. Правда проверку на пустоту стека я делаю неявную - по факту возврата None
# при получении скобки из стека (это для варианта с одной скобкой, т.к. для второго решение принимается по факту неравенства None с ожидаемой скобкой).
# Для варианта с несколькими типами скобок используется словарь.

# 4. Стек
# 7.* Добавьте в стек функцию, возвращающую текущий минимальный элемент в нём за O(1)
# Реализовано точно по рекомендованному алгоритму - через стек минимумов, без лишних проверок.

# 4. Стек
# 8.* Добавьте в стек функцию, которая возвращает среднее значение всех элементов в стеке. Она должна выполняться за O(1).
# Здесь также без сюрпризов - реализовано через внутреннюю переменную. Правда я забыл ее сделать приватной.

# 4. Стек
# 9*. Напишите функцию, которая с помощью двух стеков реализует вычисление постфиксных выражений.
# Реализовано согласно рекомендованному алгоритму. По вычислению аргументов в одной строке - у меня была как раз такая ошибка
# в первом прохождении данного курса - в этот раз я ее не допустил, значения параметров получаю заранее.
# Операции реализованы через лямбды (но об этом я и в прошлый раз тоже догадался).


